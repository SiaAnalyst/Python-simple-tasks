def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


print(solution(4))  # return 3
print(solution(6))  # return 8
print(solution(16))  # return 60
print(solution(3))  # return 0
print(solution(5))  # return 3
print(solution(15))  # return 45
print(solution(0))  # return 0
print(solution(-1)) # return 0
print(solution(10)) # return 23
print(solution(20)) # return 78
print(solution(200)) # return 9168