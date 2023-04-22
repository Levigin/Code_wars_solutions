def longest_palindrome(s: str):
    start = 0
    str_palindrome = ''
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if len(str_palindrome) >= j - i:
                break
            elif s[i:j] == s[i:j][::-1]:
                str_palindrome = s[i:j]

    return str_palindrome


print(longest_palindrome('ttaaftffftfaafatf'))