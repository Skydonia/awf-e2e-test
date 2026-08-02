"""Small statistics helpers for workflow tests."""

from collections.abc import Sequence


def mean(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("mean requires at least one value")
    return sum(values) / len(values)


def median(values: Sequence[float]) -> float:
    """Return the median of a non-empty sequence of numeric values."""
    if not values:
        raise ValueError("median requires at least one value")

    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def variance(values: Sequence[float]) -> float:
    """Return the population variance of a non-empty sequence."""
    if not values:
        raise ValueError("variance requires at least one value")

    average = mean(values)
    return sum((value - average) ** 2 for value in values) / len(values)


def standard_deviation(values: Sequence[float]) -> float:
    """Return the population standard deviation of a non-empty sequence."""
    return variance(values) ** 0.5
