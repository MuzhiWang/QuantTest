from Config.StockConfig import StockCode, StockDataType
from Core.Provider.TuShare import TuShare
from Database.MongoDB import Client
import Common.StringUtils as str_utils
import pandas as pd
import bson
import datetime
import json
from Common import DatetimeUtils
import unittest



class Test1(unittest.TestCase):

    csv_path = ".\\test1.csv"

    # @unittest.skip
    def test_mongodb_client(self):
        ts = TuShare()
        mongodb_client = Client.Client()
        start_date = "2019-09-01"
        end_date = "2019-09-04"

        ttt = str_utils.date_to_object_id(start_date)
        print(ttt)

        for stock in StockCode.Test:
            df = ts.get_1min_stock_price(stock, start_date, end_date)
            # df = pd.read_csv(csv_path)
            print(df.head(10))
            # df.to_csv(csv_path, index=False)
            # t_df = pd.read_csv(csv_path)
            # print(t_df.head(10))
            # print(t_df.to_json())

            mongodb_client.upsert_stock_price_df(stock, StockDataType.Daily, df, start_date)
            print("success to insert stock %s . with df: %s" % (stock, df.to_json()))

            get_rec = mongodb_client.get_stock_price_df(stock, StockDataType.Daily, start_date)
            if get_rec is not None:
                print(get_rec.head(10))
            # break

    # @unittest.skip
    def test_mongodb_client_get_record_no_record(self):
        mongodb_client = Client.Client()
        start_date = "2019-09-03"
        stock = "000001"
        res = mongodb_client.get_record(StockDataType.Daily, stock, start_date)
        print(res)

    @unittest.skip
    def test_mongodb_client_get_stock_price_df(self):
        mongodb_client = Client.Client()
        start_date = "2019-09-02"
        end_date = "2019-09-03"
        stock = "000001"
        res = mongodb_client.get_stock_price_df(stock, StockDataType.Daily, start_date, end_date)
        print(res.to_string())

        r1 = mongodb_client.get_stock_price_df(stock, StockDataType.Daily, start_date, start_date)
        r2 = mongodb_client.get_stock_price_df(stock, StockDataType.Daily, end_date, end_date)
        # print(r1.head(10))
        # print(r2.head(10))
        # print(r1.append(r2))

    @unittest.skip
    def test_datetime_utils(self):
        start_date = "2018-10-01"
        end_date = "2018-10-11"
        print(DatetimeUtils.get_interval_dates(start_date, end_date))


if __name__ == '__main__':
    unittest.main()
