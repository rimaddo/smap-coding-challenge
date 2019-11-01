from typing import Dict, List

import pandas as pd

from consumption.models import Consumption


def get_user_consumption_by_time_of_day() -> List[Dict[int, int]]:
    # Query for data and put into dataframe
    df = pd.DataFrame(list(Consumption.objects.all().values()))

    # Add hour of day column
    df['hour'] = pd.to_datetime(df['datetime'], format='%H:%M:%S').dt.hour

    # Average
    average_df = df[['hour', 'amount']].groupby(['hour'], as_index=False).mean()

    # Return as list of dicts
    return average_df.to_dict('records')
