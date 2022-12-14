def total_salary(path):
    fh = open(path, 'r')
    lines = fh.readlines()
    sum = 0.0
    list = []
    for i in lines:
        list.append(i.rstrip('\n').split(','))
    for j in list:
        sum += float(int(j[1]))
    fh.close()
    return sum