def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum += value
    return sum


print(amount_payment([20, 10, 12, 13, 14]))