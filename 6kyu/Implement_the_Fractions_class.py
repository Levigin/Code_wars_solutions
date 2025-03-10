class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator
        self.top, self.bottom = Fraction.get_short_fraction(self.top, self.bottom)

    # Equality test
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __add__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        new_numeration = first_num + second_num
        new_denominator = self.bottom * other.bottom
        first, second = self.get_short_fraction(new_numeration, new_denominator)
        return Fraction(first, second)

    @staticmethod
    def get_short_fraction(num, denom):
        i = 1
        while i < num and i < denom:
            if num % i == 0 and denom % i == 0:
                num //= i
                denom //= i
            i += 1
        return num, denom

    def __str__(self):
        return f'{self.top}/{self.bottom}'

    def __repr__(self):
        return str(self)


a = Fraction(399, 207)
b = Fraction(720, 102)
print(a + b)
