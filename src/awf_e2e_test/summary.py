"""Statistical summaries for numeric sequences."""

from collections.abc import Sequence
from dataclasses import dataclass

from .statistics import mean, median


@dataclass(frozen=True)
class StatisticsSummary:
    """Immutable summary statistics for a non-empty sequence."""

    count: int
    mean: float
    median: float
    minimum: float
    maximum: float


def describe(values: Sequence[float]) -> StatisticsSummary:
    """Return count, central tendency, and range for ``values``."""
    return StatisticsSummary(
        count=len(values),
        mean=mean(values),
        median=median(values),
        minimum=min(values),
        maximum=max(values),
    )
