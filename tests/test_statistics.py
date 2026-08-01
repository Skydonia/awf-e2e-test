import pytest

from awf_e2e_test.statistics import mean


def test_mean() -> None:
    assert mean([1, 2, 3, 4]) == 2.5


def test_mean_empty() -> None:
    with pytest.raises(ValueError):
        mean([])
