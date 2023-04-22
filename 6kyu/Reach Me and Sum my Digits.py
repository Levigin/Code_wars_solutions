def sumDig_nthTerm(initVal, patternL, nthTerm):
    n = nthTerm - 1
    curr_value = n // len(patternL)
    limit = n % len(patternL)
    sum_pattern = sum(patternL) * curr_value
    curr_res = sum_pattern + initVal

    for i in range(limit):
        curr_res += patternL[i]

    list_digit = [int(j) for j in list(str(curr_res))]

    return sum(list_digit)


# print(sumDig_nthTerm(10, [2, 1, 3], 16))
# print(sumDig_nthTerm(10, [2, 1, 3], 157))
print(sumDig_nthTerm(100, [2, 2, 5, 8], 157))
