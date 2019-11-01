import logging
import os
from collections import defaultdict
from time import time
from typing import DefaultDict, Dict, List, Optional, Tuple

import pandas as pd
from django.db.models import Model

from consumption.models import Area, Consumption, Tariff, User
from consumption.utils import csv_to_df

log = logging.getLogger(__name__)

CSV_EXTENSION = '.csv'
USER_DATA_EXPECTED_COLUMNS = ['id', 'area', 'tariff']
CONSUMPTION_DATA_EXPECTED_COLUMNS = ['user', 'datetime', 'consumption']

LOOKUPS_TYPE = DefaultDict[type(Model), Dict[Tuple, Model]]


def import_data(user_filepath: Optional[str] = None, consumption_folderpath: Optional[str] = None) -> None:

    # User data
    if user_filepath is not None:
        log.info('Importing user data....')
        start = time()

        user_df = csv_to_df(filpath=user_filepath)
        import_user_data(df=user_df)

        log.info(f'Finished importing users. Took: {round(time() - start, 2)} secs')

    # Consumption Data
    if consumption_folderpath is not None:
        log.info('Importing consumption data...')
        count, start = 0, time()

        for file in os.listdir(consumption_folderpath):
            if CSV_EXTENSION in file:
                log.info(f'Importing data from {file} ({round(time() - start, 2)} secs)')

                df = csv_to_df(filpath=f'{consumption_folderpath}/{file}')
                df['user'] = file.replace(CSV_EXTENSION, '')
                import_consumption_data(df=df)
                count += 1

        log.info(f'Finished importing consumption from {count} files. Took: {round(time() - start, 2)} secs')


def import_user_data(df: pd.DataFrame) -> None:
    """Function for importing user data and saving to the database."""

    # Check as expected
    check_df_columns(df=df, expected_columns=USER_DATA_EXPECTED_COLUMNS)
    # Update column names
    df.rename(columns={'id': 'external_id'}, inplace=True)

    # Memory management - faster to store repeat references in a dict than re-get_or_create
    lookups: LOOKUPS_TYPE = defaultdict(dict)

    # Create each user and reference data if doesn't already exist
    for user in df.to_dict('records'):
        # Update with foreign keys
        user.update({
            'area': get_or_create(model=Area, lookups=lookups, name=user['area']),
            'tariff': get_or_create(model=Tariff, lookups=lookups, name=user['tariff']),
        })
        # Create user instance
        get_or_create(model=User, lookups=lookups, **user)


def import_consumption_data(df: pd.DataFrame) -> None:
    """Function for importing consumption data and saving to the database."""

    # Check as expected
    check_df_columns(df=df, expected_columns=CONSUMPTION_DATA_EXPECTED_COLUMNS)
    # Update column names
    df.rename(columns={'user': 'user__external_id', 'consumption': 'amount'}, inplace=True)

    # Memory management - faster to store repeat references in a dict than re-get_or_create
    lookups: LOOKUPS_TYPE = defaultdict(dict)

    # Create each user and reference data if doesn't already exist
    for consumption in df.to_dict('records'):
        # Update with foreign keys
        consumption.update({
            'user': get_or_create(model=User, external_id=consumption['user__external_id'], lookups=lookups),
        })
        # Create user instance
        get_or_create(model=Consumption, lookups=lookups, **consumption)


def check_df_columns(df: pd.DataFrame, expected_columns: List[str]) -> None:
    if set(df.columns) != set(expected_columns):
        raise RuntimeError(
            'Exited because expected columns %s in df but got columns %s!!',
            set(expected_columns),
            set(df.columns),
        )


def get_or_create(model: type(Model), lookups: LOOKUPS_TYPE, **kwargs) -> Model:
    """Get or create model via looking up the models name directly"""
    key = tuple(kwargs.values())
    if key not in lookups[model]:
        instance, created = model.objects.get_or_create(**kwargs)
        lookups[model][key] = instance
    return lookups[model][key]
