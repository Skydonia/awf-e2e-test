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


def standard_deviation(values: Sequence[float]) -> float:
    """Return the population standard deviation of a non-empty sequence."""
    if not values:
        raise ValueError("standard_deviation requires at least one value")

    average = mean(values)
    variance = sum((value - average) ** 2 for value in values) / len(values)
    return variance**0.5
