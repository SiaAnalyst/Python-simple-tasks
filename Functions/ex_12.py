def modeling(factor, *numbers, correction):
    result = 0
    for number in numbers:
        result += number * factor
    result = result - correction
    return result


print(modeling(10, 1, 2, 3, correction=2))  # 58