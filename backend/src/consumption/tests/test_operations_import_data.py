from datetime import datetime

import pandas as pd
import pytest

from consumption.models import Area, Consumption, Tariff, User
from consumption.operations.import_data import import_consumption_data, import_user_data


@pytest.mark.django_db
def test_import_user_data():
    # Define input
    df = pd.DataFrame([
        {'id': 100, 'area': 'Area 1', 'tariff': 'Tariff A'},
        {'id': 101, 'area': 'Area 2', 'tariff': 'Tariff B'},
    ])

    # Run import
    import_user_data(df=df)

    # Assert data imported
    assert Area.objects.get(name='Area 1')
    assert Area.objects.get(name='Area 2')
    assert Tariff.objects.get(name='Tariff A')
    assert Tariff.objects.get(name='Tariff B')
    assert User.objects.get(external_id=100, area__name='Area 1', tariff__name='Tariff A')
    assert User.objects.get(external_id=101, area__name='Area 2', tariff__name='Tariff B')


def test_import_consumption_data():
    # Define input
    df = pd.DataFrame([
        {'user': 100, 'datetime': '2019-01-01 00:00:00', 'consumption': 10},
        {'user': 200, 'datetime': '2019-01-01 00:00:00', 'consumption': 1},
    ])

    # Run import
    import_consumption_data(df=df)

    # Assert data imported
    assert User.objects.get(external_id=100)
    assert User.objects.get(external_id=200)
    assert Consumption.objects.get(user__external_id=100, datetime=datetime(2019, 1, 1), amount=10)
    assert Consumption.objects.get(user__external_id=200, datetime=datetime(2019, 1, 1), amount=1)

