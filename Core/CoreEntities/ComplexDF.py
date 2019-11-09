import pandas as pd


class ComplexDF(object):
    df: pd.DataFrame = None
    expected_dates = []
    missed_dates = []

    def __init__(self, df: pd.DataFrame, expected_dates: [], missed_dates: []):
        self.df = df
        self.expected_dates = expected_dates
        self.missed_dates = missed_dates
