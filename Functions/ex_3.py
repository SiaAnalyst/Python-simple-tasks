def add_ten(a):
    b = 10
    return a + b


print(add_ten(6))  # 16


a = 5
b = 0


def fun():
    global a
    a = 10
    b = 2


fun()
print(a)  # 10
print(b)  # 0