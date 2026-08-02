import pytest

from awf_e2e_test.calculator import add, divide, power, subtract


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract_positive_integers() -> None:
    assert subtract(7, 3) == 4


def test_subtract_negative_result() -> None:
    assert subtract(3, 7) == -4


def test_subtract_decimal_values() -> None:
    assert subtract(2.5, 1.25) == pytest.approx(1.25)


def test_subtract_zero() -> None:
    assert subtract(5, 0) == 5


def test_power_positive_integer_exponent() -> None:
    assert power(2, 3) == 8


def test_power_zero_exponent() -> None:
    assert power(7, 0) == 1


def test_power_negative_exponent() -> None:
    assert power(2, -2) == pytest.approx(0.25)


def test_power_decimal_base() -> None:
    assert power(1.5, 2) == pytest.approx(2.25)


def test_divide() -> None:
    assert divide(9, 3) == 3


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
