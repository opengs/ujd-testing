import pytest


@pytest.mark.parametrize("numerator,denominator,expected_numerator,expected_denominator", [
    (10, 10, 1, 1),
])
def test_create(self, numerator, denominator, expected_numerator, expected_denominator):