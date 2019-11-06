import enum

class StockDataType(enum.Enum):
    Daily = 0
    OneHour = 1
    ThirtyMins = 2
    TenMins = 3
    FiveMins = 4
    OneMin = 5

class StockCode:
    Test = ["000001", "000002", "000003"]
