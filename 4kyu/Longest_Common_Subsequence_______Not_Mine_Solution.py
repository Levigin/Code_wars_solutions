# Recursive
def lcs(x, y):
    if x == '' or y == '':
        return ''
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    else:
        left = lcs(x[:-1], y)
        right = lcs(x, y[:-1])

    return left if len(left) > len(right) else right


# DYNAMIC PROGRAMMING
def fill_dyn_matrix(x, y):
    L = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    for i, x_elem in enumerate(x):
        for j, y_elem in enumerate(y):
            if x_elem == y_elem:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max((L[i][j - 1], L[i - 1][j]))
    return L


def LCS_DYN(x, y):
    L = fill_dyn_matrix(x, y)
    LCS = []
    x_i, y_i = len(x) - 1, len(y) - 1
    while x_i >= 0 and y_i >= 0:
        if x[x_i] == y[y_i]:
            LCS.append(x[x_i])
            x_i, y_i = x_i - 1, y_i - 1
        elif L[x_i - 1][y_i] > L[x_i][y_i - 1]:
            x_i -= 1
        else:
            y_i -= 1
    LCS.reverse()
    return LCS


print(LCS_DYN("abcdefghijklmnopq", "zapcdefghijklmnobq"))
