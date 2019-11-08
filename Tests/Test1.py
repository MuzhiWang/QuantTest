from Config.StockConfig import StockCode, StockDataType
from Gateway.TuShare import TuShare_GW
from Database.MongoDB import Client
import Common.StringUtils as str_utils
from Common import DatetimeUtils
import unittest
import bson
from Gateway.JQData import JQData_GW



class Test1(unittest.TestCase):

    csv_path = ".\\test1.csv"
    mongodb_client = Client.Client()
    jqdate_client = JQData_GW()

    @unittest.skip
    def test_mongodb_client(self):
        ts = TuShare_GW()
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

            self.mongodb_client.upsert_stock_price_df(stock, StockDataType.Daily, df, start_date)
            print("success to insert stock %s . with df: %s" % (stock, df.to_json()))

            get_rec = self.mongodb_client.get_stock_price_df(stock, StockDataType.Daily, start_date)
            if get_rec is not None:
                print(get_rec.head(10))
            # break

    @unittest.skip
    def test_mongodb_client_get_record_no_record(self):
        start_date = "2019-09-03"
        stock = "000001"
        res = self.mongodb_client.get_record(StockDataType.Daily, stock, str_utils.date_to_object_id(start_date))
        print(res)

    @unittest.skip
    def test_mongodb_client_get_stock_price_df(self):

        start_date = "2019-09-02"
        end_date = "2019-09-03"
        stock = "000001"
        res = self.mongodb_client.get_stock_price_df(stock, StockDataType.Daily, start_date, end_date)
        print(res.to_string())

        r1 = self.mongodb_client.get_stock_price_df(stock, StockDataType.Daily, start_date, start_date)
        r2 = self.mongodb_client.get_stock_price_df(stock, StockDataType.Daily, end_date, end_date)
        # print(r1.head(10))
        # print(r2.head(10))
        # print(r1.append(r2))

    @unittest.skip
    def test_datetime_utils(self):
        start_date = "2018-10-01"
        end_date = "2018-10-11"
        print(DatetimeUtils.get_interval_dates(start_date, end_date))

    # @unittest.skip
    def test_test_test(self):
        print(bson.ObjectId())
        print(bson.ObjectId("5dc5166437b0ee6779f63918"))
        print(DatetimeUtils.get_days_between_dates("2019-10-01", "2019-10-03"))

    @unittest.skip
    def test_mongodb_get_and_store_dates_status(self):
        self.mongodb_client.save_dates(StockDataType.Daily, "000001", "2019-01-11", "2019-02-01")
        res = self.mongodb_client.get_store_dates(StockDataType.Daily, "000001")
        print(res)

    @unittest.skip
    def test_jqdata_client(self):
        print(self.jqdate_client.get_1min_bars("000001", 10, "2019-10-10"))



if __name__ == '__main__':
    unittest.main()
