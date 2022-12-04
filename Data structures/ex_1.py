colors = ['red', 'green', 'blue']
print(colors)

persons = ['Jane', 'Steve', 'Moris']
print(persons[1])  # Steve

persons = ['Jane', 'Steve', 'Moris']
persons[1] = 'Niv'
print(persons)  # ['Jane', 'Niv', 'Moris']

data = [4, 3, 7.5]
sum = 0
for value in data:
    sum = sum + value
print(sum)  # 14.5