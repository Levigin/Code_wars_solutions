def binarray(s):
    count = 0
    max_len = -1
    dict_value = {0: -1}
    if len(s) < 1:
        return 0
    for i in range(0, len(s)):
        if s[i] == 0:
            count += 1
        else:
            count -= 1
        if count not in dict_value:
            dict_value[count] = i
        else:
            max_len = max(max_len, i - dict_value[count])

    return max_len


l = [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1]
print(binarray(l))