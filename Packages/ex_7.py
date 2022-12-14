def data_preparation(list_data):
    list = []
    for i in list_data:
        if len(i) > 2:
            i.remove(max(i))
            i.remove(min(i))
            for j in i:
                list.append(j)
        else:
            for j in i:
                list.append(j)
    list.sort(key=None, reverse=True)
    return list