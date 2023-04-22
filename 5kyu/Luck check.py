def luck_check(string):

    left_border = 0
    right_border = len(string) - 1
    sum_left = 0
    sum_right = 0

    while left_border < right_border:
        try:
            sum_right += int(string[right_border])
            sum_left += int(string[left_border])
            right_border -= 1
            left_border += 1
        except:
            return 'It should give an error for invalid input'

    if sum_left == sum_right:
        return True

    return False


print(luck_check('68A341179'))