def jumbled_string(s, n):
    count = 0
    k = 1
    curr_s = s
    s = s[::2] + s[1::2]
    while s != curr_s:
        s = s[::2] + s[1::2]
        k += 1
    n -= (n//k) * k

    while count != n:
        s = s[::2] + s[1::2]
        count += 1

    return s


print(jumbled_string('@DS9}UAWd', 5))
