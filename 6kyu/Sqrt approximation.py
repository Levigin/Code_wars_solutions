def sqrt_approximation(number):
    i = 1
    while True:

        if i * i == number:
            return i
        elif i * i <= number < (i + 1) * (i + 1):
            return [i, i + 1]

        i += 1


print(sqrt_approximation(124124124))
