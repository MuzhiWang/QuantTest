import enum
from Config.StockConfig import StockDataSource

class IndustryCode(enum.Enum):
    sw_l1 = 0 # 申万一级行业
    sw_l2 = 1 # 申万二级行业
    sw_l3 = 2 # 申万三级行业
    jq_l1 = 3 # 聚宽一级行业
    jq_l2 = 4 # 聚宽二级行业
    zjw = 5  # 证监会行业


class Constant:
    DATE_INDEX = {
        StockDataSource.TUSHARE: "trade_time",
        StockDataSource.JQDATA: "date",
        StockDataSource.TDX: "date"
    }

    TDX_BLOCK_CODE_LIST = 'code_list'
    TDX_BLOCK_NAME = 'blockname'

class TDX_BLOCK_NAME:
    HUSHENG_300 = '沪深300'
    ZHONGZHENG_100 = '中证100'
    ZHONGZHENG_200 = '中证200'
    CHUANGYEBANZHI = '创业板指'
    ZHONGZHENGHONGLI = '中证红利'

