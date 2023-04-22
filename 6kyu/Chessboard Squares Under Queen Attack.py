def chessboard_squares_under_queen_attack(a, b):
    aggregated_value = 0
    for j in range(a):
        for i in range(b):
            aggregated_value += count_cells_under_attack(a, b, j, i)
    return aggregated_value - 4 * a * b


def count_cells_under_attack(a: int, b: int, start_j: int, start_i: int):
    ans = 0
    if 0 <= start_j < a and 0 <= start_i < b:
        j, i = start_j, start_i
        ans += a + b - 2
        while j >= 0 and i >= 0:
            ans += 1
            j -= 1
            i -= 1
        j, i = start_j, start_i
        while j >= 0 and i < b:
            ans += 1
            j -= 1
            i += 1
        j, i = start_j, start_i
        while j < a and i < b:
            ans += 1
            j += 1
            i += 1
        j, i = start_j, start_i
        while j < a and i >= 0:
            ans += 1
            j += 1
            i -= 1
        return ans
    else:
        return -1


print(chessboard_squares_under_queen_attack(2500, 2500)) # Говно способ
