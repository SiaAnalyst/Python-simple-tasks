num = float(input("Enter number: "))

if num > 0:
    result = "Positive number"
elif num == 0:
    result = "Zero"
else:
    result = "Negative number"

print(result)

work_experience = int(input("Enter your full work experience in years: "))

if work_experience > 1 and work_experience <= 5:
    developer_type = "Middle"
elif work_experience <= 1:
    developer_type = "Junior"
else:
    developer_type = "Senior"

print(developer_type)