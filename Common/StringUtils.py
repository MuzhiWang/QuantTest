import datetime
import bson



def date_to_object_id(date_time: str):
    if len(date_time) != 10:
        raise Exception("date length doesn't equal to 8")
    time = datetime.datetime.strptime(date_time, '%Y-%m-%d')
    return bson.ObjectId.from_datetime(time)