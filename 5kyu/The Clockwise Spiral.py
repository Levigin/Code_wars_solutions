def create_spiral(n):
    if type(n) == str:
        return []
    matrix = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(j)
        matrix.append(temp)

    val = 1
    m = 0

    matrix[n//2][n//2] = n * n
    for j in range(n // 2):

        for i in range(n - m):
            matrix[j][i + j] = val
            val += 1

        for i in range(j + 1, n - j):
            matrix[i][-j - 1] = val
            val += 1

        for i in range(j + 1, n - j):
            matrix[-j - 1][-i - 1] = val
            val += 1

        for i in range(j + 1, n - (j + 1)):
            matrix[-i - 1][j] = val
            val += 1

        m += 2

    return matrix


print(create_spiral(1050))


