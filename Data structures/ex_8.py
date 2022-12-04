def lookup_key(data, value):
    key_list = []
    for k, v in data.items():
        if v == value:
            key_list.append(k)
    return key_list

