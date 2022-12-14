import random


def get_random_winners(quantity, participants):
    if quantity > len(participants):
        return []
    else:
        result = list(participants.keys())
        random.shuffle(result)
        winners = random.sample(result, k=quantity)
        return winners