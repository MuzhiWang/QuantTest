import pandas as pd
import enum


class DF_MA(object):
    df: pd.DataFrame = None
    start_date = None
    end_date = None
    missed_dates = []

    ma_dict = {}

    def __init__(
            self, df: pd.DataFrame, start_date: str, end_date: str, ma_days: []):
        self.df = df
        self.start_date = start_date
        self.end_date = end_date
        self.ma_dict = {}
        # self.missed_dates = missed_dates

        if ma_days is None:
            raise Exception("must define MA days")


class MACatogary(enum.Enum):
    UNDEFINED = 0
    THIRTY_DAYS = 1
    TWNTY_DAYS = 2
    FIFTEEN_DAYS = 3
    TEN_DAYS = 4
    EIGHT_DAYS = 5
    FIVE_DAYS = 6

class Constant:
    ma_category_mins_map = {
        MACatogary.UNDEFINED: -1,
        MACatogary.THIRTY_DAYS: 7200,
        MACatogary.TWNTY_DAYS: 4800,
        MACatogary.FIFTEEN_DAYS: 3600,
        MACatogary.TEN_DAYS: 2400,
        MACatogary.EIGHT_DAYS: 1920,
        MACatogary.FIVE_DAYS: 1200
    }