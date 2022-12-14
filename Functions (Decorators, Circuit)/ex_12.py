from functools import reduce


def amount_payment(payment):
    return reduce((lambda sum, x: (sum + x) if(x>0) else sum), payment, 0)