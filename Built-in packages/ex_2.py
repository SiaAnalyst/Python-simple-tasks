from datetime import date
from calendar import monthrange


def get_days_in_month(month, year):
    days = monthrange(year, month)[1]
    return days