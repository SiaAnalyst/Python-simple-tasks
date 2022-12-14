from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    sum = Decimal("0")
    for i in number_list:
        sum += Decimal(str(i))
    getcontext().prec = signs_count
    avg_value = Decimal(sum) / Decimal(str(len(number_list)))
    return avg_value