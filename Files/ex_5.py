def get_cats_info(path):
    lines = []
    with open(path, 'r') as f:
        for i in f.readlines():
            lines.append(i.strip('\n').split(','))
    cats_info = []
    for i in lines:
        dict = {}
        dict['id'] = i[0]
        dict['name'] = i[1]
        dict['age'] = i[2]
        cats_info.append(dict)
    return cats_info
