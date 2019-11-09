import pandas as pd


class DF_MA(object):
    df: pd.DataFrame = None
    start_date = None
    end_date = None
    missed_dates = []

    ma_dict = {}

    def __init__(
            self, df: pd.DataFrame, start_date: str, end_date: str, missed_dates: [], ma_days: []):
        self.df = df
        self.start_date = start_date
        self.end_date = end_date
        self.missed_dates = missed_dates

        if ma_days is None:
            raise Exception("must define MA days")

