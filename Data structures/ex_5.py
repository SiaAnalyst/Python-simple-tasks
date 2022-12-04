greeting = "Hello my little friend"
hello = greeting[0:5]

print(greeting)
print(hello)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[0:10:2]
even_numbers = numbers[1:10:2]
three_numbers = numbers[2:10:3]

print(odd_numbers)
print(even_numbers)
print(three_numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2:10:3]

numbers_copy = numbers[:]

print(odd_numbers)
print(even_numbers)
print(three_numbers)
print(numbers_copy)