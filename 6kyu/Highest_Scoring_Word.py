def high(x):
    score_letters = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
        'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
        'z': 26
    }
    score = 0
    score_max = 0
    i = 0
    word = None
    while i < len(x):
        j = i
        while j < len(x) and x[j] != ' ':
            score += score_letters[x[j]]
            j += 1
        if score_max < score:
            score_max = score
            word = x[i: j]
        score = 0
        i = j + 1

    return word


# print(high('man i need a taxi up to ubud'))
# print(high('what time are we climbing up the volcano'))
# print(high('b aa'))
# print(high('aaa b'))
# print(high('d bb'))
print(high(''))