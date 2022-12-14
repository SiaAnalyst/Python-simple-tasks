from datetime import datetime, timedelta


def get_days_from_today(date):
    date_new = date.split('-')
    date = datetime(int(date_new[0]), int(date_new[1]), int(date_new[2])).date()
    current_date = datetime.now().date()
    delta = current_date - date
    return delta.days