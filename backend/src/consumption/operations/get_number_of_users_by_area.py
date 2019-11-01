from typing import Dict, List

import pandas as pd
from django.db.models import F

from consumption.models import User


def get_number_of_users_by_area() -> List[Dict[int, int]]:
    # Query for data and put into dataframe
    df = pd.DataFrame(list(User.objects.annotate(area_name=F('area__name')).all().values()))

    # Count
    count_df = df[['external_id', 'area_name']].groupby(['area_name'], as_index=False).size().reset_index(name='counts')

    # Return as list of dicts
    return count_df.to_dict('records')
