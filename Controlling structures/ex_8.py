for variable in range(5):
    print(variable)  # 0 1 2 3 4

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for i in message:
    if i == search:
        result += 1
print(result)