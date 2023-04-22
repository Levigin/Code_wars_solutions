from collections import deque


def get_symbols(math_expression: str):
    math_symbol = []
    opening = dict()
    closing = dict()

    deq = deque()

    i = 0
    while i < len(math_expression):
        if math_expression[i] == ' ':
            i += 1
            continue

        if math_expression[i].isdigit():
            j = i
            while i + 1 < len(math_expression) and (math_expression[i].isdigit() or math_expression[i + 1] == '.'):
                i += 1
                if i >= len(math_expression):
                    break
            number = float(math_expression[j: i])
            math_symbol.append(number)
        else:
            if math_expression[i] == '(':
                deq.append(len(math_symbol))
            elif math_expression[i] == ')':
                close_index = len(math_symbol)
                opening[close_index] = deq.pop()
                closing[opening[close_index]] = close_index

            math_symbol.append(math_expression[i])
            i += 1
    # print(math_symbol)
    return math_symbol, opening, closing


def parentheses(l_border, r_border, math_symb: list, opening: dict, closing: dict):
    index = l_border
    simply_expressions = []
    while index <= r_border:
        if math_symb[index] == "(":
            simply_expression = parentheses(index + 1, closing[index] - 1, math_symb, opening, closing)
            simply_expressions.append(simply_expression)
            index = closing[index]
        else:
            simply_expressions.append(math_symb[index])

        index += 1
    get_math_expression = get_none_negative(simply_expressions)
    print(simply_expressions)

    return calculate(get_math_expression)


def calculate(math_expression: list) -> float:
    def recursive_seeker(curr_index: int, curr_mult_div: float, result: float,
                         last_operation_is_mult_div: bool) -> float or None:

        print(f'curr_index: {curr_index}, curr_mult_div: {curr_mult_div}, result: {result}')

        # base case
        if len(math_expression) == 0:
            return None

        # border case:
        if curr_index >= len(math_expression):
            return result + curr_mult_div

        if math_expression[curr_index] == '+':
            return recursive_seeker(curr_index + 1, 1.0, result + curr_mult_div, False)

        elif math_expression[curr_index] == '-':
            return recursive_seeker(curr_index + 1, -1.0, result + curr_mult_div, False)

        if last_operation_is_mult_div:

            if math_expression[curr_index] == '*':
                curr_mult_div *= math_expression[curr_index + 1]
            elif math_expression[curr_index] == '/':
                curr_mult_div /= math_expression[curr_index + 1]
            return recursive_seeker(curr_index + 2, curr_mult_div, result, True)

        else:
            curr_mult_div *= math_expression[curr_index]
            return recursive_seeker(curr_index + 1, curr_mult_div, result, True)

    return recursive_seeker(0, 1.0, 0.0, False)


def get_none_negative(math_expression: list):
    math_expression_without_neg = []
    if len(math_expression) == 0:
        return None

    if math_expression[0] == '-':
        math_expression_without_neg.append(-math_expression[1])
        index = 2
    else:
        index = 0

    while index < len(math_expression):
        if index + 2 < len(math_expression) and math_expression[index] in ['/', '-', '*', '+'] and \
                math_expression[index + 1] == '-':
            math_expression_without_neg.append(math_expression[index])
            math_expression_without_neg.append(-math_expression[index + 1 + 1])
            index += 3
        else:
            math_expression_without_neg.append(math_expression[index])
            index += 1

    return math_expression_without_neg


def math_expres(math_expression: str):
    math_symb, op_symp, cl_symp = get_symbols(math_expression)
    return parentheses(0, len(math_symb) - 1, math_symb, op_symp, cl_symp)


print(math_expres("-7 * -(6 / 3)"))
