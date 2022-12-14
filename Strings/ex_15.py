import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"(http[s]?://[^.]+[.]?[^.]+[.]\w{2,3})", text)
    for match in iterator:
        result.append(match.group())
    return result