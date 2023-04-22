def generate_diagonal(n, l):
    list_triangle = []
    res = []
    for j in range(l + n):
        list_triangle.append([])
        list_triangle[j].append(1)
        for k in range(1, j):
            list_triangle[j].append(list_triangle[j - 1][k - 1] + list_triangle[j - 1][k])
        if l != 0 and len(list_triangle) != 1:
            list_triangle[j].append(1)

    curr = 0
    for i in range(n, l + n):
        res.append(list_triangle[i][curr])
        curr += 1

    return res


print(generate_diagonal(2, 5))