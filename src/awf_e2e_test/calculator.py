"""Small arithmetic helpers for workflow tests."""


def add(left: float, right: float) -> float:
    return left + right


def subtract(left: float, right: float) -> float:
    """Return ``left`` minus ``right``."""
    return left - right


def power(base: float, exponent: float) -> float:
    """Return ``base`` raised to ``exponent``."""
    return base**exponent


def divide(left: float, right: float) -> float:
    if right == 0:
        raise ZeroDivisionError("division by zero")
    return left / right
