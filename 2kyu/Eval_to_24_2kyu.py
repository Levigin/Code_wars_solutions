import operator

operator_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


def equal_to_24(a, b, c, d):
    digits_list = [a, b, c, d]
    return recursive_seeker(digits_list, 0, '', 0, '', 24)


def recursive_seeker(digits_remainder: list, curr_sum: int, expression: str, curr_par_sum, curr_par_expr, target=24):
    if len(digits_remainder) == 0 and curr_sum == target and len(curr_par_expr) == 0:
        return expression
    if curr_sum + curr_par_sum == target and len(digits_remainder) == 0:
        return expression + f'+{curr_par_expr}'
    elif len(digits_remainder) == 0 and len(curr_par_expr) == 0:

        return 'not'
    else:
        for digit in digits_remainder:
            new_digits_remained = digits_remainder[:]
            new_digits_remained.remove(digit)

            if len(curr_par_expr) == 0:

                for key, value in operator_dict.items():
                    if not (key == '*' and key == '/' and len(digits_remainder) == 4):
                        result = recursive_seeker(new_digits_remained, operator_dict[key](curr_sum, digit), (f'({expression})' if key == '*' or key == '/' else expression) + f"{key}{digit}", curr_par_sum, curr_par_expr, target)
                        if result != 'not':
                            return result

                result = recursive_seeker(new_digits_remained, curr_sum, expression, curr_par_sum + digit, curr_par_expr + f'+{digit}', target)
                if result != 'not':
                    return result
                result = recursive_seeker(new_digits_remained, curr_sum, expression, curr_par_sum - digit, curr_par_expr + f'-{digit}', target)
                if result != 'not':
                    return result
            else:
                for key, value in operator_dict.items():
                    result = recursive_seeker(new_digits_remained, curr_sum, expression, operator_dict[key](curr_par_sum, digit), '(' + curr_par_expr + f'){key}{digit}', target)
                    if result != "not":
                        return result

        if len(expression) != 0 and len(curr_par_expr) != 0:
            result = recursive_seeker(digits_remainder, curr_sum * curr_par_sum, f'({expression})*({curr_par_expr})', 0, '', target)
            if result != 'not':
                return result
            if curr_par_sum != 0:
                result = recursive_seeker(digits_remainder, curr_sum / curr_par_sum, f'({expression})/({curr_par_expr})', 0, '', target)
                if result != 'not':
                    return result

    return "not"


print(equal_to_24(8, 16, 69, 36))



