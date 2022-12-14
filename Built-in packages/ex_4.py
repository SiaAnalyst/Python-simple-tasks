from random import randrange


def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000 and min < quantity < max:
        result = set()
        while len(result) < quantity:
            result.add(randrange(min, max))

        result = list(result)
        result.sort()
        return result
    else:
        return []