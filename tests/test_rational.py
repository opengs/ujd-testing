import pytest

from src.rational import Rational

@pytest.mark.parametrize("numerator,denominator,expected_numerator,expected_denominator", [
    (10, 10, 1, 1),
    (10, 5, 2, 1),
    (10, -10, -1, 1),
    (1, 2, 1, 2),
])
def test_create(numerator, denominator, expected_numerator, expected_denominator):
    rational = Rational(numerator, denominator)
    assert rational.numerator == expected_numerator
    assert rational.denominator == expected_denominator

@pytest.mark.parametrize("numerator,denominator,result", [
    (1, 1, 1),
    (1, 2, 0.5),
    (2, 4, 0.5),
    (0, 2, 0),
])
def test_to_float(numerator: int, denominator: int, result: float):
    rational = Rational(numerator, denominator)
    #float comparison
    assert abs(rational.to_float() - result) < 0.0001

@pytest.mark.parametrize("numerator_a, denominator_a, numerator_b, denominator_b, expected_numerator, expected_denominator", [
    (1, 1, 1, 1, 2, 1),
    (1, 1, -1, 1, 0, 1),
    (1, 2, 1, 3, 5, 6)
])
def test_plus(numerator_a, denominator_a, numerator_b, denominator_b, expected_numerator, expected_denominator):
    a = Rational(numerator_a, denominator_a)
    b = Rational(numerator_b, denominator_b)
    result = a.plus(b)
    assert result.numerator == expected_numerator
    assert result.denominator == expected_denominator

@pytest.mark.parametrize("numerator_a, denominator_a, numerator_b, denominator_b, expected_numerator, expected_denominator", [
    (1, 1, 1, 1, 0, 1),
    (1, 1, -1, 1, 2, 1),
    (1, 1, 1, 6, 5, 6),
])
def test_minus(numerator_a, denominator_a, numerator_b, denominator_b, expected_numerator, expected_denominator):
    a = Rational(numerator_a, denominator_a)
    b = Rational(numerator_b, denominator_b)
    result = a.minus(b)
    assert result.numerator == expected_numerator
    assert result.denominator == expected_denominator

@pytest.mark.parametrize("numerator_a, denominator_a, numerator_b, denominator_b, expected_numerator, expected_denominator", [
    (1, 1, 1, 1, 1, 1),
    (1, 1, -1, 1, -1, 1),
    (2, 3, 5, 7, 10, 21),
])
def test_times(numerator_a, denominator_a, numerator_b, denominator_b, expected_numerator, expected_denominator):
    a = Rational(numerator_a, denominator_a)
    b = Rational(numerator_b, denominator_b)
    result = a.times(b)
    assert result.numerator == expected_numerator
    assert result.denominator == expected_denominator

@pytest.mark.parametrize("numerator_a, denominator_a, numerator_b, denominator_b, expected_numerator, expected_denominator", [
    (1, 1, 1, 1, 1, 1),
    (1, 1, -1, 1, -1, 1),
    (2, 3, 5, 7, 14, 15),
])
def test_divides(numerator_a, denominator_a, numerator_b, denominator_b, expected_numerator, expected_denominator):
    a = Rational(numerator_a, denominator_a)
    b = Rational(numerator_b, denominator_b)
    result = a.divides(b)
    assert result.numerator == expected_numerator
    assert result.denominator == expected_denominator

@pytest.mark.parametrize("numerator_a, denominator_a, numerator_b, denominator_b, expected_numerator, expected_denominator", [
    (1, 1, 1, 1, 1, 1),
    (1, 1, 2, 1, 3, 2),
    (2, 3, 5, 7, 7, 10),
    (2, 3, -5, 7, -3, 10),
])
def test_mediant(numerator_a, denominator_a, numerator_b, denominator_b, expected_numerator, expected_denominator):
    a = Rational(numerator_a, denominator_a)
    b = Rational(numerator_b, denominator_b)
    result = a.mediant(b)
    assert result.numerator == expected_numerator
    assert result.denominator == expected_denominator

@pytest.mark.parametrize("numerator_a, denominator_a, numerator_b, denominator_b, result", [
    (1, 1, 1, 1, 0),
    (1, 1, 2, 1, -1),
    (2, 1, 1, 1, 1),
])
def test_compare_to(numerator_a, denominator_a, numerator_b, denominator_b, result):
    a = Rational(numerator_a, denominator_a)
    b = Rational(numerator_b, denominator_b)
    assert a.compare_to(b) == result

@pytest.mark.parametrize("numerator_a, denominator_a, numerator_b, denominator_b, result", [
    (1, 1, 1, 1, True),
    (1, 1, 2, 1, False),
    (2, 1, 1, 1, False),
    (2, 4, 3, 6, True),
])
def test_equals(numerator_a, denominator_a, numerator_b, denominator_b, result):
    a = Rational(numerator_a, denominator_a)
    b = Rational(numerator_b, denominator_b)
    assert a.equals(b) == result

    

@pytest.mark.parametrize("numerator, denominator, expected_numerator, expected_denominator", [
    (1, 1, -1, 1),
    (1, -1, 1, 1),
    (2, 1, -2, 1),
    (2, 4, -1, 2),
    (0, 1, 0, 1)
])
def test_negate(numerator, denominator, expected_numerator, expected_denominator):
    rational = Rational(numerator, denominator)
    result = rational.negate()
    assert result.numerator == expected_numerator
    assert result.denominator == expected_denominator

@pytest.mark.parametrize("numerator, denominator, expected_numerator, expected_denominator", [
    (1, 1, 1, 1),
    (1, -1, 1, 1),
    (2, 1, 2, 1),
    (2, 4, 1, 2),
    (0, 1, 0, 1)
])
def test_abs(numerator, denominator, expected_numerator, expected_denominator):
    rational = Rational(numerator, denominator)
    result = rational.abs()
    assert result.numerator == expected_numerator
    assert result.denominator == expected_denominator

@pytest.mark.parametrize("numerator, denominator, expected_numerator, expected_denominator", [
    (1, 1, 1, 1),
    (-1, 1, -1, 1),
    (2, 1, 1, 2)
])
def test_reciprocal(numerator, denominator, expected_numerator, expected_denominator):
    rational = Rational(numerator, denominator)
    result = rational.reciprocal()
    assert result.numerator == expected_numerator
    assert result.denominator == expected_denominator