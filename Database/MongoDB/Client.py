import pymongo
from Config.StockConfig import StockDataType, StockDataSource
import Common.StringUtils as str_utils
import json
import string
import bson
from Database.MongoDB.MongoDBConfig import *
import pandas as pd
from Common import DatetimeUtils
from Gateway.Config import Constant as gw_const
from Common.Log.Logger import Logger
from Common.Exception import UnimplementedException


class Client(object):
    client = None
    __local_host = "mongodb://localhost:27017/"

    def __init__(self):
        self.client = pymongo.MongoClient(self.__local_host)
        self.__logger = Logger.get_logger(__name__)

        # Check database exists
        dblist = self.client.list_database_names()
        self.__logger.debug("db list: " + ', '.join(dblist))

    def get_stock_record_by_id(self, stock_data_source: StockDataSource, stock_data_type: StockDataType, collection_id: str,
                               record_id: bson.ObjectId):
        db = self.client[self.__get_db_name(stock_data_source, stock_data_type)]
        # if stock_data_type == StockDataType.DAILY:
        records = db[collection_id].find({Constant.ID: record_id})
        for r in records:
            return r
        return None

    def get_record_by_id(self, database_name: str, collection_id: str,
                         record_id: bson.ObjectId):
        db = self.client[database_name]
        records = db[collection_id].find({Constant.ID: record_id})
        for r in records:
            return r

    def query_records(self, database_name: str, collection_id: str,
                         query_dict: {}):
        db = self.client[database_name]
        return db[collection_id].find(query_dict)

    def query_stock_records(self, stock_data_source: StockDataSource, stock_data_type: StockDataType, collection_id: str,
                            query_dict: {}):
        db = self.client[self.__get_db_name(stock_data_source, stock_data_type)]
        if stock_data_type == StockDataType.DAILY or \
                stock_data_type == StockDataType.FIVE_MINS or \
                stock_data_type == StockDataType.ONE_MIN:
            records = db[collection_id].find(query_dict)
            return records
        else:
            raise UnimplementedException

    def upsert_record(
            self, stock_data_source: StockDataSource, stock_data_type: StockDataType, collection_id: str, record: dict,
            record_id: bson.ObjectId = None):
        db = self.client[self.__get_db_name(stock_data_source, stock_data_type)]

        if record_id is None:
            record_id = bson.ObjectId()

        if stock_data_type == StockDataType.DAILY or \
            stock_data_type == StockDataType.FIVE_MINS or \
                stock_data_type == StockDataType.ONE_MIN:
            cur_collection = db[collection_id]
            myquery = {Constant.ID: record_id}
            newvalues = {"$set": record}

            cur_collection.update_one(myquery, newvalues, upsert=True)
        else:
            raise Exception("unimplemented")

    def get_stored_dates(self, stock_data_source: StockDataSource, stock_data_type: StockDataType, collection_id: str):
        res = self.get_stock_record_by_id(stock_data_source, stock_data_type, collection_id, Constant.STORED_DATES_STATUS_ID)
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
        if start_date is None or end_date is None:
            raise Exception('start date and end date must exist in getting stock price df')

        if stock_data_type == StockDataType.DAILY or \
                stock_data_type == StockDataType.FIVE_MINS or \
                stock_data_type == StockDataType.ONE_MIN:
            # all_dates = DatetimeUtils.get_interval_dates(start_date, end_date)
            all_df = pd.DataFrame()

            query_dict = {
                Constant.TRADE_DATE: {
                    '$lt': DatetimeUtils.convert_date_str_to_int(end_date),
                    '$gte': DatetimeUtils.convert_date_str_to_int(start_date)
                }
            }
            self.__logger.debug(f'query stock {stock_id} dict: {query_dict}')
            records = self.query_stock_records(stock_data_source, stock_data_type, stock_id, query_dict)

            if records is None:
                return None

            for rec in records:
                json_obj = json.loads(rec[Constant.DATAFRAME])
                rec_df = pd.DataFrame(json_obj)
                all_df = all_df.append(rec_df, ignore_index=True)

            # Get records one by one
            # empty_records = []
            # for date in all_dates:
            #     get_rec = self.get_record_by_id(stock_data_source, StockDataType.DAILY, stock_id,
            #                                     str_utils.date_to_object_id(date))
            #     if get_rec is None:
            #         empty_records.append(date)
            #         continue
            #     json_obj = json.loads(get_rec[Constant.DATAFRAME])
            #     rec_df = pd.DataFrame(json_obj)
            #     all_df = all_df.append(rec_df, ignore_index=True)
            #     # print(all_df.count())
            # self.__logger.debug(f"\nget EMPTY record for {stock_id} in source {stock_data_source.name} of dates: {empty_records}")

            if all_df.empty:
                return None

            rec_sort_df = all_df.sort_values(gw_const.DATE_INDEX[stock_data_source], ascending=True)

            return rec_sort_df
        else:
            raise Exception('unimplemented')

    def upsert_stock_price_df(
            self, stock_data_source: StockDataSource, stock_data_type: StockDataType, stock_id: str, df_data, date=None):
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
        elif stock_data_type == StockDataType.FIVE_MINS or \
                stock_data_type == StockDataType.ONE_MIN:
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

    def __get_db_name(self, stock_data_source: StockDataSource, stock_data_type: StockDataType):
        return f"{stock_data_source.name}_{stock_data_type.name}"
