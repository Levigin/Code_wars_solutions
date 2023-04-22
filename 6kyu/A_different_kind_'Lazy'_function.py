from typing import Callable


def lazy(n: int):
    def deco(func: Callable):
        counter = 0

        def wrapper(*args, **kwargs):
            nonlocal counter
            print(f'{counter = }, {n = }')
            if n > 0:
                if n == 1 or counter == 0:
                    counter += 1
                    return func(*args, **kwargs)
                elif counter % n == 0:
                    counter += 1
                    return func(*args, **kwargs)
                else:
                    counter += 1
                    return None
            else:
                counter -= 1
                if n == -1:
                    return None
                elif counter % n != 0:
                    return func(*args, **kwargs)
        return wrapper
    return deco


@lazy(4)
def sum_(a, b):
    return a + b


print(f'{sum_(2,2) = }')
