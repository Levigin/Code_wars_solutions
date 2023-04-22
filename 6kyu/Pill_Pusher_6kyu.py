def prescribe(d, a, b):
    result = 0
    value1 = d // a
    value2 = d // b
    for i in range(value1 + 1):
        for j in range(value2 + 1):
            if result <= d and (a * i + b * j) <= d:
                result = max(result, a * i + b * j)

    return result


print(prescribe(180, 25, 60))
