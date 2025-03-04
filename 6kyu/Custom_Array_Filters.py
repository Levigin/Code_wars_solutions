class list:

    def __init__(self, array):
        self.array = array
        self.res = []

    def even(self):
        for val in self.array:
            if self.is_integer(val) and val % 2 == 0:
                self.res.append(val)
        return self.res

    def odd(self):
        for val in self.array:
            if self.is_integer(val) and val % 2 != 0:
                self.res.append(val)
        return self.res

    def over(self, num: int):
        for val in self.array:
            if self.is_integer(val) and val > num:
                self.res.append(val)
        return self.res

    def under(self, num: int):
        for val in self.array:
            if self.is_integer(val) and val < num:
                self.res.append(val)
        return self.res

    def in_range(self, i: int, j: int):
        for val in self.array:
            if self.is_integer(val) and i <= val <= j:
                self.res.append(val)
        return self.res

    @staticmethod
    def is_integer(val) -> bool:
        return True if isinstance(val, int) else False

    def __str__(self):
        return f'{self.array}'

    def __repr__(self):
        return str(self.array)


obj = list(["a", 1, "b", 300, "x", "q", 63, 122, 181, "z", 0.83, 0.11]).even()
print(obj)
# obj = list([1, 2, 3, 4, 5])
# print(obj.odd())
# obj = list(["a", "b", "c"])
# print(obj.under(4))
# obj = list(["a", "b", "c"])
# print(obj.over(4))
# obj = list([1, 2, 3, 4, 5])
# print(obj.over(10))
# obj = list([1, 2, 3, 4, 5])
# print(obj.in_range(1, 3))


