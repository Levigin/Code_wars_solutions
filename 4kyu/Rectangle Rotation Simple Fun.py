def rectangle_rotation(a, b):
    # First rectangle
    a_1 = (a / (2 ** 0.5)) / 2
    b_1 = (b / (2 ** 0.5)) / 2
    a_new = (int(a_1)*2 + 1)
    b_new = (int(b_1)*2 + 1)

    # Second rectangle
    if a_1 - int(a_1) < 0.5:
        a_2 = a_new - 1
    else:
        a_2 = a_new + 1

    if b_1 - int(b_1) < 0.5:
        b_2 = b_new - 1
    else:
        b_2 = b_new + 1

    res = a_new * b_new + a_2 * b_2
    return res


print(rectangle_rotation(6, 4))
