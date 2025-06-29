import random

def get_numbers_ticket(min_value, max_value, quantity):
    if (
        isinstance(min_value, int)
        and isinstance(max_value, int)
        and isinstance(quantity, int)
        and min_value >= 1
        and max_value <= 1000
        and min_value <= max_value
        and quantity <= (max_value - min_value + 1)
    ):
        lottery_ticket = random.sample(range(min_value, max_value + 1), quantity)
        return sorted(lottery_ticket)
    else:
        return []