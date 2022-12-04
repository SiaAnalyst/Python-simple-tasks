num = [1, 3.1415, 41, 3]
num.append(30)
print(num)  # [1, 3.1415, 41, 3, 30]


num = [1, 3.1415, 41, 3]
num.insert(2, 30)
print(num)  # [1, 3.1415, 30, 41, 3]


num = [1, 3.1415, 41, 3]
second = num.pop(1)
print(second)  # 3.1415
print(num)  # [1, 41, 3]


num = [1, 3.1415, 41, 3]
num.remove(3.1415)
print(num)  # [1, 41, 3]


num = [1, 3.1415, 41, 3]
new_num = sorted(num)
print(new_num)  # [1, 3, 3.1415, 41]
print(num)  # [1, 3.1415, 41, 3]