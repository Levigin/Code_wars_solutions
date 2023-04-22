def solution(args):
    res_str = ''
    i = 0
    while i < len(args) - 1:
        if abs(args[i] - args[i + 1]) != 1:
            res_str += str(args[i]) + ','
            i += 1
            if i == len(args) - 1:
                res_str += str(args[i])
                return res_str
        else:
            j = i + 1
            num = args[i]
            while j < len(args) and abs(args[j] - num) == 1:
                j += 1
                num += 1

            if j - i - 1 > 1:
                res_str += str(args[i]) + '-' + str(args[j - 1]) + ','
                i = j
                if i == len(args) - 1:
                    res_str += str(args[i]) + ','
            else:
                if i + 1 == len(args) - 1:
                    res_str += str(args[i]) + ',' + str(args[j - 1]) + ','
                    i += 1
                else:
                    res_str += str(args[i]) + ','
                    i += 1

    return res_str[:-1]


# print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
# print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
print(solution([-78, -75, -73, -71, -69, -66, -63, -60, -57, -55, -54, -53, -52, -51, -48]))
# print(solution([-99, -98, -97, -96, -93, -91, -88, -85, -83, -80, -79]))
# print(solution([-69, -68, -65, -64, -62, -61, -58, -55, -53, -51, -49, -47, -44, -43, -41, -39, -37, -35, -34, -33, -31, -28, -25,-24, -22, -19]))
# print(solution([-57, -54, -53, -51, -50, -47, -44, -42, -39, -37, -34, -32, -31, -29, -26, -23, -21, -19, -16, -14, -12, -9, -6, -4, -2, -1, 2]))

