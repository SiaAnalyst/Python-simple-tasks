# Calculate the factorial of number n using recursion
# @param n - the number for which to calculate the factorial
# @return - the factorial of number n
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter positive number: "))
result = factorial(num)
print(f"Factorial of {num} is equal {result}")