def two_sum(numbers, target):
    dict_numbers = {}

    for i, j in enumerate(numbers):
        if target - j in dict_numbers:
            return [dict_numbers[target - j], i]
        dict_numbers[j] = i


print(two_sum([2, 2, 3], 4))