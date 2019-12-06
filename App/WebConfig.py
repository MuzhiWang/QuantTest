from Config.StockConfig import StockDataType
from enum import  Enum
from Controller.Entities.DF_MA import MACatogary
from Gateway.Config import TDX_BLOCK_NAME


class BlockCategory(Enum):
    INDEX = 0
    INDUSTRY = 1


class Constants:
    DATE_TYPE = {
        "1min": StockDataType.ONE_MIN,
        "5min": StockDataType.FIVE_MINS,
        "day": StockDataType.DAILY
    }

    BLOCK_DICT = {
        "index": BlockCategory.INDEX,
        "industry": BlockCategory.INDUSTRY
    }

    MA_DICT = {
        "5d": MACatogary.FIVE_DAYS,
        "8d": MACatogary.EIGHT_DAYS,
        "10d": MACatogary.TEN_DAYS,
        "15d": MACatogary.FIFTEEN_DAYS,
        "20d": MACatogary.TWNTY_DAYS,
        "30d": MACatogary.THIRTY_DAYS
    }

    INDEX_DICT = {
        "zhongzheng100": TDX_BLOCK_NAME.ZHONGZHENG_100,
        "zhongzheng200": TDX_BLOCK_NAME.ZHONGZHENG_200,
        "zhongzhenghongli": TDX_BLOCK_NAME.ZHONGZHENGHONGLI,
        "hushen300": TDX_BLOCK_NAME.HUSHENG_300,
        "chuangyebanzhi": TDX_BLOCK_NAME.CHUANGYEBANZHI
    }
