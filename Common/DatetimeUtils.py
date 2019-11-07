from Common.StringUtils import *
from datetime import date, timedelta

def GetIntervalDates(start_date, end_date):
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
