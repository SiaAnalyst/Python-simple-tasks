is_access = True
message = "Welcome" if is_access else "Forbidden"

some_data = None
message2 = some_data or "Not data"

num = int(input("Enter an integer number: "))
is_even = True if num%2 == 0 else False
print(is_even)
