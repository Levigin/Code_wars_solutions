def matrix_addition(a, b):
    c = []
    d = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            d.append(a[i][j] + b[i][j])
        c.append(d)
        d = []

    return c


print(matrix_addition([[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]))