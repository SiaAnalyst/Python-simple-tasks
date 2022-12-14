def flatten(data):
    if data == []:
        return data
    if isinstance(data[0], list):
        return flatten(data[0]) + flatten(data[1:])
    return data[:1] + flatten(data[1:])