import math

class Rational():
    pass

class Rational():
    '''Represents rational number'''

    def __init__(self, numerator: int, denominator: int) -> None:
        self._numerator = numerator
        self._denominator = denominator
        self.__reshape()

    @property
    def numerator(self) -> int:
        return self._numerator

    @property
    def denominator(self) -> int:
        return self._denominator

    def to_float(self) -> float:
        return self._numerator / self._denominator

    def plus(self, other: Rational) -> Rational:
        new_denominator = self._denominator * other.denominator
        new_numerator = self._numerator*other.denominator + other.numerator*self.denominator
        self._numerator = new_numerator
        self._denominator = new_denominator
        self.__reshape()
        return self

    def minus(self, other: Rational) -> Rational:
        new_denominator = self._denominator * other.denominator
        new_numerator = self._numerator*other.denominator - other.numerator*self.denominator
        self._numerator = new_numerator
        self._denominator = new_denominator
        self.__reshape()
        return self

    def times(self, other: Rational) -> Rational:
        self._numerator = self._numerator*other.numerator
        self._denominator = self._denominator*other.denominator
        self.__reshape()
        return self

    def divides(self, other: Rational) -> Rational:
        self._numerator = self._numerator*other.denominator
        self._denominator = self._denominator*other.numerator
        self.__reshape()
        return self

    def mediant(self, other: Rational) -> Rational:
        self._numerator = self._numerator + other.numerator
        self._denominator = self._denominator + other.denominator
        self.__reshape()
        return self

    def compareTo(self, other: Rational) -> int:
        result = self.to_float() - other.to_float()
        return -1 if result < 0 else 1 if result > 0 else 0

    def compareTo(self, other: Rational) -> bool:
        return self.denominator == other.denominator and self.numerator == other.numerator

    def to_string(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def negate(self) -> Rational:
        self._numerator = -self._numerator
        return self

    def abs(self) -> Rational:
        self._numerator = abs(self._numerator)
        self._denominator = abs(self._denominator)
        return self

    def reciprocal(self) -> Rational:
        tmp = self._numerator
        self._numerator = self.denominator
        self._denominator = tmp
        return self

    def __reshape(self):
        a = abs(self.numerator)
        b = abs(self.denominator)
        while a*b != 0:
            if a >= b:
                a = a % b
            else:
                b = b % a
        divider = a + b
        self._numerator = round(self._numerator / divider)
        self._denominator = round(self._denominator / divider)

    