def decode(data):
    if not data:
        return []
    return [data[0]]*data[1] + decode(data[2:])