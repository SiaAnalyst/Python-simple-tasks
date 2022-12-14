import re


def find_all_emails(text):
    result = re.findall(r"[A-Za-z]+[.\w-]+@\w+[.]{1}[\w-]{2,}", text)
    return result