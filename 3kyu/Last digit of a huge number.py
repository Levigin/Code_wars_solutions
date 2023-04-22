def last_digit(lst):
    power = 1
    for base in reversed(lst):
        power = (base if base < 2 else (base - 2) % 20 + 2) ** (
                     power if power < 2 else (power - 2) % 4 + 2)
    return power % 10


print(last_digit([7, 6, 21]))
