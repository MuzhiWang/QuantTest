from Gateway.TuShare import TuShare_GW
from Config.StockConfig import *
from Database.MongoDB import Client
from Config.StockConfig import StockDataType


class OnlineSyncTask(object):

    def __init__(self):
        pass

    def sync(self):
        ts = TuShare_GW()
        mongodb_client = Client.Client()
        start_date = '20181001'
        end_date = '20181011'
        for stock in StockCode.Test:
            df = ts.get_1min_stock_price(stock, start_date, end_date)
            record = mongodb_client.upsert_stock_price_df(StockDataSource.TUSHARE, StockDataType.DAILY, stock, df, )
            print("success to insert stock %s , record id: %s. with df: %s" % (stock, record.inserted_id, df.to_json()))
            break


sync = OnlineSyncTask()
sync.sync()