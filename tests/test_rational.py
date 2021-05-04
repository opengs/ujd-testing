import pytest

from src.rational import Rational

@pytest.mark.parametrize("numerator,denominator,expected_numerator,expected_denominator", [
    (10, 10, 1, 1),
    (10, 5, 2, 1),
    (10, -10, -1, 1),
    (1, 2, 1, 2),
])
def test_create(self, numerator, denominator, expected_numerator, expected_denominator):
    rational = Rational(numerator, denominator)
    assert rational.numerator == expected_numerator
    assert rational.denominator == expected_denominator