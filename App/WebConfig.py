from Config.StockConfig import StockDataType

class Constants:
    DATE_TYPE = {
        "1min": StockDataType.ONE_MIN,
        "5min": StockDataType.FIVE_MINS,
        "day": StockDataType.DAILY
    }