def sum_strings(x, y):
    # Check null element on beginning string
    if len(x) > 1 and len(y) > 1:
        i = 0
        while i < len(x) and x[i] == '0':
            i += 1
        x = x[i:]
        i = 0
        while i < len(y) and y[i] == '0':
            i += 1
        y = y[i:]

    if x == '' and y != '':
        return y
    elif x != '' and y == '':
        return x

    index_x = len(x) - 1
    index_y = len(y) - 1
    curr_value = 0
    result = ''

    while index_y >= 0 and index_x >= 0:

        if int(x[index_x]) + int(y[index_y]) + curr_value > 9:
            result = str(((int(x[index_x]) + int(y[index_y])) + curr_value) % 10) + result
            curr_value = 1
        else:
            result = str((int(x[index_x]) + int(y[index_y])) + curr_value) + result
            curr_value = 0

        index_y -= 1
        index_x -= 1

        if index_x < 0 and index_y >= 0:
            if curr_value == 1:
                while index_y >= 0:
                    if int(y[index_y]) + curr_value > 9:
                        result = str((curr_value + int(y[index_y])) % 10) + result
                    else:
                        result = str(int(y[index_y]) + curr_value) + result
                        curr_value = 0
                        break
                    index_y -= 1
                if index_y >= 0:
                    result = y[:index_y] + result
            else:
                result = y[:index_y + 1] + result

        if index_y < 0 and index_x >= 0:
            if curr_value == 1:
                while index_x >= 0:
                    if int(x[index_x]) + curr_value > 9:
                        result = str((curr_value + int(x[index_x])) % 10) + result
                    else:
                        result = str(int(x[index_x]) + curr_value) + result
                        curr_value = 0
                        break
                    index_x -= 1
                if index_x >= 0:
                    result = x[:index_x] + result
            else:
                result = x[:index_x + 1] + result

    if curr_value == 1:
        result = '1' + result

    if result == '':
        return '0'

    return result


def sum_string_new(x: str, y: str):
    if len(x) > 1 and len(y) > 1:
        i = 0
        while i < len(x) and x[i] == '0':
            i += 1
        x = x[i:]
        i = 0
        while i < len(y) and y[i] == '0':
            i += 1
        y = y[i:]
    result = []
    new_x = list(map(int, x))
    new_y = list(map(int, y))

    if len(new_x) > len(new_y):
        new_x, new_y = new_y, new_x

    j = len(new_y) - 1
    count_position = 0
    position_one = [0 for _ in range(len(new_y) + 1)]
    for i in range(len(new_x) - 1, -1, -1):
        if new_y[j] + new_x[i] + position_one[count_position] > 9:
            position_one[count_position + 1] = 1
        result.append((new_y[j] + new_x[i]) % 10)
        j -= 1
        count_position += 1

    print(f'j = {j}')
    print(f'result = {result}')

    result += reversed(new_y[:j + 1])

    result.reverse()
    position_one.reverse()
    index_new_y = len(new_y) - 1
    for m in range(len(position_one) - 1, len(position_one) - len(new_y) - 1, -1):
        if result[index_new_y] + position_one[m] > 9:
            position_one[m - 1] = 1
            result[index_new_y] = 0
        else:
            result[index_new_y] = result[index_new_y] + position_one[m]
        index_new_y -= 1

    if position_one[0] == 1:
        result = [1] + result
    result = list(map(str, result))
    print(f'position_one = {position_one}')
    return ''.join(result)


print(sum_string_new('712569312664357328695151392', '8100824045303269669937'))
print(712569312664357328695151392 + 8100824045303269669937)
# print(sum_string_new("99999999999999996543213", "14646646513215498498498"))
# print(99999999999999996543213 + 14646646513215498498498)
# print(sum_string_new("9999", "1222"))
# print(9999 + 1222)
# print(sum_string_new("2999", "302"))
# print(2999 + 302)
# print(sum_string_new("101", "399"))
# print(101 + 399)
# print(sum_string_new("9999999999999999", "1"))
# print(9999999999999999 + 1)
# start = time.time_ns()
# print(sum_string_new("800", "9567"))
# end = time.time_ns()
# print(f'time {(end - start) // 10 ** 6} millisecond')
