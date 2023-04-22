import numpy as np


def rotate_like_a_vortex(matrix):
    matrix_new = np.array(matrix)
    ring = len(matrix) // 2
    i = 0

    while i < ring:
        j = i + 1
        while j > 0:
            temp_one = list(reversed([k for k in matrix_new[i, i: len(matrix_new) - i]]))
            temp_two = [k for k in matrix_new[i:len(matrix) - i, i]]
            temp_tree = list(reversed([k for k in matrix_new[len(matrix_new) - 1 - i, i: len(matrix_new) - i]]))
            temp_four = [k for k in matrix_new[i:len(matrix) - i, len(matrix_new) - i - 1]]
            matrix_new[i:len(matrix) - i, i] = temp_one
            matrix_new[len(matrix_new) - 1 - i, i: len(matrix_new) - i] = temp_two
            matrix_new[i:len(matrix) - i, len(matrix_new) - i - 1] = temp_tree
            matrix_new[i, i: len(matrix_new) - i] = temp_four
            j -= 1
        i += 1

    curr_matrix = []

    for n in range(len(matrix_new)):
        temp = []
        for m in range(len(matrix_new[0])):
            temp.append(matrix_new[n][m])
        curr_matrix.append(temp)

    return curr_matrix


matrix = [ [ 5, 3, 6, 1 ],
          [ 5, 8, 7, 4 ],
          [ 1, 2, 4, 3 ],
          [ 3, 1, 2, 2 ] ]

# expected = [[1, 4, 3, 2],
#             [6, 4, 2, 2],
#             [3, 7, 8, 1],
#             [5, 5, 1, 3]]
print(rotate_like_a_vortex(matrix))