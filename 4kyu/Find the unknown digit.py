def solve_runes(runes: str):

    for i in range(10):
        text = runes.replace('?', str(i))
        expressions_list = get_list_expression(text)
        if expressions_list and str(i) not in runes:
            for item in range(len(expressions_list)):
                if item == 0 and expressions_list[item] == '-':
                    expressions_list[item + 1] *= -1
                    expressions_list[item] = ''
                elif expressions_list[item - 1] in ['-', '+', '=', '*'] and expressions_list[item] == '-':
                    expressions_list[item + 1] *= -1
                    expressions_list[item] = ''
            for expr in expressions_list:
                if expr == '':
                    expressions_list.remove(expr)

            for num in range(len(expressions_list)):
                if expressions_list[num] == '*':
                    if expressions_list[num - 1] * expressions_list[num + 1] == expressions_list[-1]:
                        return i
                elif expressions_list[num] == '-':
                    if expressions_list[num - 1] - expressions_list[num + 1] == expressions_list[-1]:
                        return i
                elif expressions_list[num] == '+':
                    if expressions_list[num - 1] + expressions_list[num + 1] == expressions_list[-1]:
                        return i
    return -1


def get_list_expression(expression: str):
    express_list = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit() or expression[i] == '?':
            j = i
            while j < len(expression) and expression[j] not in ['=', '+', '-', '*']:
                j += 1
            temp = expression[i:j]
            if temp[0] == '0' and len(temp) > 1:
                return False
            express_list.append(int(temp))
            i = j
        else:
            express_list.append(expression[i])
            i += 1
    return express_list


# print(solve_runes("1+1=?"))
# print(solve_runes("-5?*-1=5?"))
# print(solve_runes("19--45=5?"))
print(solve_runes("123?45*?=?"))
# print(solve_runes("?*123?45=?"))

