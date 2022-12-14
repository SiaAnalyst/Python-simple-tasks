from collections import UserList
from functools import reduce


class AmountPaymentList(UserList):
    def amount_payment(self):
        return reduce((lambda sum, x: (sum + x) if (x > 0) else sum), self.data, 0)