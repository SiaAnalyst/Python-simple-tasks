from functools import reduce


def sum_numbers(numbers):
    return reduce((lambda sum, x: sum + x), numbers, 0)