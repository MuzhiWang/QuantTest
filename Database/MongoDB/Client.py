import pymongo
from Config.StockConfig import StockDataType
import Common.StringUtils as str_utils
import json
import string
import bson

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

    def get_record(self, stock_data_type: StockDataType, collection_id, date):
        if stock_data_type == StockDataType.Daily:
            records = self.stock_daily_db[collection_id].find({'_id': str_utils.date_to_object_id(date)})
            for r in records:
                return r

    def get_stock_price(self, stock_id, stock_data_type, start_date = None, end_date = None):
        if stock_data_type == StockDataType.Daily:
            if start_date == None:
                start_date = "20190101"
            if end_date == None:
                end_date = "20191010"


    def upsert_stock_price(self, stock_id: str, stock_date_type, df_data, date=None):
        if stock_date_type == StockDataType.Daily:
            if date is None:
                raise Exception("no date for daily stock price insert")
            # collect_lists = self.stock_daily_db.list_collection_names()
            cur_collection = self.stock_daily_db[stock_id]
            # dicts = df_data.to_dict()
            dicts = {
                "_id": str_utils.date_to_object_id(date),
                "df": "test_dffdsafdsafdsa"
            }
            # dicts['_id'] = str_utils.date_to_object_id(date)
            # tt = json.dumps(dict, separators = (",", ":")).replace("\"", "'")
            # ttt = df_data.to_json()
            # print(tt)
            # print(ttt)

            print("correct: ")
            correct = json.loads(df_data.to_json())
            print(correct)
            print("\n\n")

            myquery = {"_id": str_utils.date_to_object_id(date)}
            newvalues = {"$set": dicts}

            cur_collection.update_one(myquery, newvalues, upsert=True)
        elif stock_date_type == StockDataType.FiveMins:
            pass
        elif stock_date_type == StockDataType.OneMin:
            pass