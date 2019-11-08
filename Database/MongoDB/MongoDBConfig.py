import bson

class StockDataNameFormat:
    Daily = 0
    OneHour = 1
    ThirtyMins = 2
    TenMins = 3
    FiveMins = 4
    OneMins = 5

class Constant:
    ID = "_id"
    TRADE_DATE = "trade_date"
    TRADE_TIME = "trade_time"
    DATAFRAME = "df"

    STORED_DATES_STATUS_ID = bson.ObjectId("5dc5166437b0ee6779f63918")
    STORED_DATES_MAP = "exist_dates"