from collections import UserString
import re

class NumberString(UserString):
    def number_count(self):
        num = []
        for number in re.findall(r'\d+', self.data):
            for i in str(number):
                num.append(i)
        return len(num)