def calculate(expression: str):

    OPERAND = ['+', '-', '$', '*']
    expr_list = []
    curr_i = 0

    for i in range(len(expression)):
        if expression[i] in OPERAND:
            expr_list.append(float(expression[curr_i: i]))
            expr_list.append(expression[i])
            curr_i = i + 1
        if not expression[i].isdigit() and expression[i] not in OPERAND and expression[i] != '.':
            return "400: Bad request"
    expr_list.append(float(expression[curr_i:]))
    print(f'expr_list = {expr_list}')

    curr_list_without_div = []
    while '$' in expr_list:
        curr_list_without_div = []
        j = 0
        while j < len(expr_list):
            if j == len(expr_list) - 1:
                curr_list_without_div.append(expr_list[j])
            else:
                if expr_list[j + 1] != '$':
                    curr_list_without_div.append(expr_list[j])
                elif expr_list[j + 1] == '$':
                    curr_list_without_div.append(expr_list[j] / expr_list[j + 2])
                    j += 3
                    break
            j += 1
        while j < len(expr_list):
            curr_list_without_div.append(expr_list[j])
            j += 1

        expr_list = curr_list_without_div
        print(f'curr_list_without_div = {curr_list_without_div}')

    curr_list_without_mult = []
    if len(curr_list_without_div) == 0:
        curr_list_without_div = expr_list
    while '*' in curr_list_without_div:
        curr_list_without_mult = []
        j = 0
        while j < len(curr_list_without_div):
            if j == len(curr_list_without_div) - 1:
                curr_list_without_mult.append(curr_list_without_div[j])
            else:
                if curr_list_without_div[j + 1] != '*':
                    curr_list_without_mult.append(curr_list_without_div[j])
                elif curr_list_without_div[j + 1] == '*':
                    curr_list_without_mult.append(curr_list_without_div[j] * curr_list_without_div[j + 2])
                    j += 3
                    break
            j += 1
        while j < len(curr_list_without_div):
            curr_list_without_mult.append(curr_list_without_div[j])
            j += 1
        curr_list_without_div = curr_list_without_mult
        print(f'curr_list_without_mult = {curr_list_without_mult}')

    if len(curr_list_without_mult) == 0 and len(curr_list_without_div) != 0:
        result = curr_list_without_div[0]
        result_list = curr_list_without_div
    elif len(curr_list_without_div) == 0 and len(curr_list_without_mult) == 0:
        result = expr_list[0]
        result_list = expr_list
    else:
        result = curr_list_without_mult[0]
        result_list = curr_list_without_mult
    j = 0
    while j < len(result_list):
        if result_list[j] == '+':
            result += result_list[j + 1]
            j += 1
        elif result_list[j] == '-':
            result -= result_list[j + 1]
            j += 1
        j += 1

    if result - int(result) != 0:
        return result

    return int(result)


print(calculate("4*3"))


