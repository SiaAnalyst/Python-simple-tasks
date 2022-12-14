def to_indexed(source_file, output_file):
    with open(source_file, 'r') as file:
        result = file.readlines()
    n = 0
    list = []
    for i in result:
        list.append(str(n) + ': ' + i)
        n+=1
    with open(output_file, 'w') as file:
        file.writelines(list)