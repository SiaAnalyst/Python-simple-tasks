from datetime import datetime


def get_str_date(date):
    date = datetime.fromisoformat(date[:-1])
    date = date.strftime('%A %d %B %Y')
    return date