def read_employees_from_file(path):
    fh = open(path, 'r')
    lines = fh.readlines()
    list = []
    for i in lines:
        list.append(i.rstrip('\n'))
    fh.close()
    return list