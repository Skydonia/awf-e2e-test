"""Small arithmetic helpers for workflow tests."""


def add(left: float, right: float) -> float:
    return left + right


def subtract(left: float, right: float) -> float:
    """Return the difference between two numeric values."""
    return left - right


def divide(left: float, right: float) -> float:
    if right == 0:
        raise ZeroDivisionError("division by zero")
    return left / right
