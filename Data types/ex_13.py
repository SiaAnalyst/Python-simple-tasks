age = input("How old are you?")
print(age)
print(type(age))

age = input("How old are you? ")
age = int(age)
print(age)
print(type(age))

pi = float('3.14')
print(pi)
print(type(pi))

pi_str = str(3.14)
age_str = str(29)

print(type(pi_str))
print(type(age_str))

print(bool(0))  # False
print(bool(1))  # True

length = "2.75"
width = "1.75"
area = float(width)*float(length)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print(show)