from Core.Provider.TuShare import TuShare
from Config.StockConfig import *
from Database.MongoDB import Client
from Config.StockConfig import StockDataType
import pandas

class SyncTask(object):

    def __init__(self):
        pass

    def sync(self):
        ts = TuShare()
        mongodb_client = Client.Client()
        start_date = '20181001'
        end_date = '20181011'
        for stock in StockCode.Test:
            df = ts.get_1min_stock_price(stock, start_date, end_date)
            record = mongodb_client.insert_stock_price(stock, StockDataType.Daily, df)
            print("success to insert stock %s , record id: %s. with df: %s" % (stock, record.inserted_id, df.to_json()))
            break


sync = SyncTask()
sync.sync()