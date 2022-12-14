import re


def generator_numbers(string=""):
    for number in re.findall(r'\d+', string):
        yield number


def sum_profit(string):
    return sum(map(int, generator_numbers(string)))
