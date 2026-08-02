import pytest

from awf_e2e_test.statistics import mean, median, standard_deviation, variance


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


def test_variance_distinct_values() -> None:
    assert variance([1, 2, 3]) == pytest.approx(2 / 3)
    assert variance([1, 2, 3, 4]) == pytest.approx(1.25)


def test_variance_decimal_values() -> None:
    assert variance([1.5, 2.5, 4.0]) == pytest.approx(1.0555555555555556)


def test_variance_empty() -> None:
    with pytest.raises(ValueError, match="variance requires at least one value"):
        variance([])


def test_variance_does_not_mutate_input() -> None:
    values = [3, 1, 2]
    variance(values)
    assert values == [3, 1, 2]


def test_standard_deviation_distinct_values() -> None:
    assert standard_deviation([1, 2, 3]) == pytest.approx((2 / 3) ** 0.5)
    assert standard_deviation([1, 2, 3, 4]) == 1.118033988749895


def test_standard_deviation_decimal_values() -> None:
    assert standard_deviation([1.5, 2.5, 4.0]) == pytest.approx(1.0274023338281628)


def test_standard_deviation_empty() -> None:
    with pytest.raises(ValueError):
        standard_deviation([])


def test_standard_deviation_does_not_mutate_input() -> None:
    values = [3, 1, 2]
    standard_deviation(values)
    assert values == [3, 1, 2]


def test_standard_deviation_is_square_root_of_variance() -> None:
    values = [1.5, 2.5, 4.0]
    assert standard_deviation(values) == pytest.approx(variance(values) ** 0.5)
