import re
def token_parser(s):
    list = []
    result = [re.split('(\d+|\D+)', p) for p in s.split(' ')]
    for i in result:
        for j in i:
            if j:
                list.append(j)
    return list