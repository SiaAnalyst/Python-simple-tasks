def make_request(keys, values):
    if len(keys) == len(values):
        dict = {keys[i]: values[i] for i in range(len(keys))}
    else:
        dict = {}
    return dict