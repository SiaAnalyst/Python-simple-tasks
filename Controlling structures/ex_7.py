num = int(input("Enter number (0 to 10): "))
count = 10 - num
i = 1
while i <= count:
    print(f"Iteration {i}")
    i = i + 1

print("End operation")

num = int(input("Enter the integer (0 to 100): "))
sum = 0
i = 1
while i <= num:
    sum += i
    i += 1
print(sum)