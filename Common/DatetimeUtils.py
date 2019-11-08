from Common.StringUtils import *
from datetime import date, timedelta

def get_interval_dates(start_date: str, end_date: str):
    if not is_date(start_date) or not is_date(end_date):
        raise Exception("start date or end date format mismatched")
    s_date = get_date(start_date)
    e_date = get_date(end_date)

    if s_date > e_date:
        raise Exception("start date later than end date")

    delta = e_date - s_date

    days = []
    for i in range(delta.days + 1):
        day = s_date + timedelta(days = i)
        days.append(str(day))

    return days


def convert_date_str_to_int(date_str: str):
    if not is_date(date_str):
        raise Exception("not date str for converting")
    return int(date_str.replace("-", ""))
