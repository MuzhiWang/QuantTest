import pymongo
from Config.StockConfig import StockDataType, StockDataSource
import Common.StringUtils as str_utils
import json
import string
import bson
from Database.MongoDB.MongoDBConfig import *
import pandas as pd
from Common import DatetimeUtils


class Client(object):
    client = None
    __local_host = "mongodb://localhost:27017/"

    def __init__(self):
        self.client = pymongo.MongoClient(self.__local_host)

        # Check database exists
        dblist = self.client.list_database_names()
        print("db list: " + ', '.join(dblist))

    def get_record(self, stock_data_source: StockDataSource, stock_data_type: StockDataType, collection_id: str,
                   record_id: bson.ObjectId):
        db = self.client[self.__get_db_name(stock_data_source, stock_data_type)]
        if stock_data_type == StockDataType.DAILY:
            records = db[collection_id].find({Constant.ID: record_id})
            for r in records:
                return r
            return None

    def upsert_record(
            self, stock_data_source: StockDataSource, stock_data_type: StockDataType, collection_id: str, record: dict,
            record_id: bson.ObjectId = None):
        db = self.client[self.__get_db_name(stock_data_source, stock_data_type)]

        if record_id is None:
            record_id = bson.ObjectId()

        if stock_data_type == StockDataType.DAILY:
            cur_collection = db[collection_id]
            myquery = {Constant.ID: record_id}
            newvalues = {"$set": record}

            cur_collection.update_one(myquery, newvalues, upsert=True)
        elif stock_data_type == StockDataType.FIVE_MINS:
            pass
        elif stock_data_type == StockDataType.ONE_MIN:
            pass

    def get_stored_dates(self, stock_data_source: StockDataSource, stock_data_type: StockDataType, collection_id: str):
        res = self.get_record(stock_data_source, stock_data_type, collection_id, Constant.STORED_DATES_STATUS_ID)
        if res is None:
            return {}
        return res[Constant.STORED_DATES_MAP]

    def save_dates(self, stock_data_source: StockDataSource, stock_data_type: StockDataType, collection_id: str,
                   start_date,
                   end_date=None):
        dates_map = self.get_stored_dates(stock_data_source, stock_data_type, collection_id)
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

        self.upsert_record(stock_data_source, stock_data_type, collection_id, dates_record,
                           Constant.STORED_DATES_STATUS_ID)

    def get_stock_price_df(
            self, stock_data_source: StockDataSource, stock_data_type: StockDataType,
            stock_id: str, start_date: str = None, end_date: str = None):
        if stock_data_type == StockDataType.DAILY:
            if start_date is None:
                start_date = "2019-01-01"
            if end_date is None:
                end_date = "2019-10-10"

            all_dates = DatetimeUtils.get_interval_dates(start_date, end_date)
            all_df = pd.DataFrame()

            for date in all_dates:
                get_rec = self.get_record(stock_data_source, StockDataType.DAILY, stock_id,
                                          str_utils.date_to_object_id(date))
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

    def upsert_stock_price_df(
            self, stock_data_source: StockDataSource, stock_data_type: StockDataType, stock_id: str, df_data, date):
        db = self.client[self.__get_db_name(stock_data_source, stock_data_type)]
        if stock_data_type == StockDataType.DAILY:
            if date is None:
                raise Exception("no date for daily stock price insert")
            cur_collection = db[stock_id]
            dicts = {
                Constant.ID: str_utils.date_to_object_id(date),
                Constant.TRADE_DATE: DatetimeUtils.convert_date_str_to_int(date),
                Constant.DATAFRAME: json.dumps(df_data.to_dict())
            }

            myquery = {Constant.ID: str_utils.date_to_object_id(date)}
            newvalues = {"$set": dicts}

            cur_collection.update_one(myquery, newvalues, upsert=True)
        elif stock_data_type == StockDataType.FIVE_MINS:
            pass
        elif stock_data_type == StockDataType.ONE_MIN:
            pass

    def __get_db_name(self, stock_data_source: StockDataSource, stock_data_type: StockDataType):
        return f"{stock_data_source.name}_{stock_data_type.name}"
