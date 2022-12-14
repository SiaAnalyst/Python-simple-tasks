def get_employees_by_profession(path, profession):
    with open(path, 'r') as file:
        result = file.readlines()
    list = []
    for i in result:
        i = i.split()
        for j in i:
            if j == profession:
                list.append(i[0])
    print(list)
    string = ' '.join(list)
    return string