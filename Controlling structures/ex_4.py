num = int(input("Enter number: "))

if num > 0:
    if num >= 100:
        result = "Positive number greater than 100"
    else:
        result = "Positive number less than 100"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"

print(result)


num = int(input("Enter a number: "))

if num > 0:
    if num%2 != 0:
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"

print(result)