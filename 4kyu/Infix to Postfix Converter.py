operators: list
priority: dict


def to_postfix(infix: str) -> str:
    global priority, operators

    priority = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4, '(': 1}
    operators = ['+', '-', '/', '*', '^']
    result = []
    dq = []

    for token in infix:
        if token.isdigit():
            result.append(token)

        elif token == '(':
            dq.append(token)

        elif token == ')':
            curr_token = dq.pop()
            while curr_token != '(':
                result.append(curr_token)
                curr_token = dq.pop()
        else:
            if token == '^':
                while len(dq) != 0 and priority[token] < priority[dq[len(dq) - 1]]:
                    result.append(dq.pop())
            else:
                while len(dq) != 0 and priority[token] <= priority[dq[len(dq) - 1]]:
                    result.append(dq.pop())

            dq.append(token)

    while len(dq) != 0:
        result.append(dq.pop())

    res_str = ''

    for i in result:
        res_str += i

    return res_str


# print(to_postfix("2^3^2"))
# print(to_postfix("(5-4-1)+9/5/2-7/1/7"))
print(to_postfix("5+(6-2)*9+3^(7-1)"))