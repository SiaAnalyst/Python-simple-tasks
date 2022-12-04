def fun(a, b=2, c=3):
    return a + b * c


print(fun(b=4, c=4, a=2))  # 18
print(fun(c=1, a=2, b=3))  # 5
print(fun(c=3, b=2, a=7))  # 13