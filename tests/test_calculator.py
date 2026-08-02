import pytest

from awf_e2e_test.calculator import add, divide, multiply


def test_add() -> None:
    assert add(2, 3) == 5


def test_multiply_positive_integers() -> None:
    assert multiply(3, 4) == 12


def test_multiply_negative_value() -> None:
    assert multiply(-3, 4) == -12


def test_multiply_decimal_values() -> None:
    assert multiply(1.5, 2.0) == pytest.approx(3.0)


def test_multiply_by_zero() -> None:
    assert multiply(7, 0) == 0


def test_divide() -> None:
    assert divide(9, 3) == 3


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
