def all_sub_lists(data):
    lists = [[]]
    for i in range(len(data) + 1):
        for j in range(i):
            lists.append(data[j: i])
    lists = sorted(lists, key=len)
    return lists