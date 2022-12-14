def write_employees_to_file(employee_list, path):
    f = open(path, 'w')
    print(employee_list)
    for i in employee_list:
        for j in i:
            f.write(j + '\n')
    f.close()