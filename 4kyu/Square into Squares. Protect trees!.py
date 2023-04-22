def decompose(n):
    value = 0
    list_value = [n]

    while list_value:
        curr_value = list_value.pop()
        value += curr_value ** 2
        curr_value -= 1
        while curr_value > 0:
            if value - (curr_value ** 2) < 0:
                curr_value = int(value ** 0.5)
            if value - (curr_value ** 2) >= 0:
                value -= curr_value ** 2
                list_value.append(curr_value)
                curr_value -= 1
                if value == 0:
                    list_value = sorted(list_value)
                    return list_value
    return None


print(decompose(498690))