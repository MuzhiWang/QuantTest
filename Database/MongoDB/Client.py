import pymongo
from Config.StockConfig import StockDataType
import Common.StringUtils as str_utils
import json
import string
import bson
from Database.MongoDB.MongoDBConfig import *
import pandas as pd
from Common import DatetimeUtils

class Client(object):

    client = None
    stock_daily_db = None
    stock_5mins_db = None
    stock_1min_db = None

    __local_host = "mongodb://localhost:27017/"
    __stock_daily_db = "stock_daily"
    __stock_5mins_db = "stock_5mins"
    __stock_1min_db = "stock_1min"

    def __init__(self):
        self.client = pymongo.MongoClient(self.__local_host)
        self.stock_daily_db = self.client[self.__stock_daily_db]
        self.stock_5mins_db = self.client[self.__stock_5mins_db]
        self.stock_1min_db = self.client[self.__stock_1min_db]

        # Check database exists
        dblist = self.client.list_database_names()
        print("db list: " + ', '.join(dblist))

    def get_record(self, stock_date_type: StockDataType, collection_id: str, record_id: bson.ObjectId):
        if stock_date_type == StockDataType.Daily:
            records = self.stock_daily_db[collection_id].find({Constant.ID: record_id})
            for r in records:
                return r
            return None

    def upsert_record(self, stock_date_type: StockDataType, collection_id: str, record: dict, record_id: bson.ObjectId = None):
        if record_id is None:
            record_id = bson.ObjectId()

        if stock_date_type == StockDataType.Daily:
            cur_collection = self.stock_daily_db[collection_id]
            myquery = {Constant.ID: record_id}
            newvalues = {"$set": record}

            cur_collection.update_one(myquery, newvalues, upsert=True)
        elif stock_date_type == StockDataType.FiveMins:
            pass
        elif stock_date_type == StockDataType.OneMin:
            pass

    def get_store_dates(self, stock_date_type: StockDataType, collection_id: str):
        res = self.get_record(stock_date_type, collection_id, Constant.STORED_DATES_STATUS_ID)
        if res is None:
            return None
        return res[Constant.STORED_DATES_MAP]

    def save_dates(self, stock_date_type: StockDataType, collection_id: str, start_date, end_date = None):
        dates_map = self.get_store_dates(stock_date_type, collection_id)
        if dates_map is None:
            dates_map = {}

        all_days = []
        if end_date is None:
            all_days.append(start_date)
        else:
            all_days = DatetimeUtils.get_interval_dates(start_date, end_date)

        for day in all_days:
            if day not in dates_map or dates_map[day] is False:
                dates_map[day] = True

        dates_record = {
            Constant.ID: Constant.STORED_DATES_STATUS_ID,
            Constant.STORED_DATES_MAP: dates_map
        }

        self.upsert_record(stock_date_type, collection_id, dates_record, Constant.STORED_DATES_STATUS_ID)


    def get_stock_price_df(self, stock_id, stock_data_type, start_date = None, end_date = None):
        if stock_data_type == StockDataType.Daily:
            if start_date == None:
                start_date = "2019-01-01"
            if end_date == None:
                end_date = "2019-10-10"

            all_dates = DatetimeUtils.get_interval_dates(start_date, end_date)
            all_df = pd.DataFrame()

            for date in all_dates:
                get_rec = self.get_record(StockDataType.Daily, stock_id, str_utils.date_to_object_id(date))
                if get_rec is None:
                    continue
                json_obj = json.loads(get_rec[Constant.DATAFRAME])
                rec_df = pd.DataFrame(json_obj)
                all_df = all_df.append(rec_df, ignore_index=True)
                print(all_df.count())

            if all_df.empty:
                return None

            rec_sort_df = all_df.sort_values(Constant.TRADE_TIME, ascending=True)

            return rec_sort_df.reset_index(drop=True)


    def upsert_stock_price_df(self, stock_id: str, stock_date_type, df_data, date=None):
        if stock_date_type == StockDataType.Daily:
            if date is None:
                raise Exception("no date for daily stock price insert")
            cur_collection = self.stock_daily_db[stock_id]
            dicts = {
                Constant.ID: str_utils.date_to_object_id(date),
                Constant.TRADE_DATE: DatetimeUtils.convert_date_str_to_int(date),
                Constant.DATAFRAME: json.dumps(df_data.to_dict())
            }

            myquery = {Constant.ID: str_utils.date_to_object_id(date)}
            newvalues = {"$set": dicts}

            cur_collection.update_one(myquery, newvalues, upsert=True)
        elif stock_date_type == StockDataType.FiveMins:
            pass
        elif stock_date_type == StockDataType.OneMin:
            pass