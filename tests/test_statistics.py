import pytest

from awf_e2e_test.statistics import mean, median


def test_mean() -> None:
    assert mean([1, 2, 3, 4]) == 2.5


def test_mean_empty() -> None:
    with pytest.raises(ValueError):
        mean([])


def test_median_odd_number_of_values() -> None:
    assert median([3, 1, 2]) == 2


def test_median_even_number_of_values() -> None:
    assert median([4, 1, 3, 2]) == 2.5


def test_median_empty() -> None:
    with pytest.raises(ValueError):
        median([])
