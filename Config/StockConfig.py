import enum

class Constant:
    MINUTES_IN_DAY = 240

class StockDataType(enum.Enum):
    UNDEFINED = 0
    DAILY = 1
    ONE_HOUR = 2
    THIRTY_MINS = 3
    TEN_MINS = 4
    FIVE_MINS = 5
    ONE_MIN = 6

class StockDataSource(enum.Enum):
    UNKNOWN = 0
    TUSHARE = 1
    JQDATA = 2
    TDX = 3



class StockCode:
    Test = ["000001", "000002", "000003"]

