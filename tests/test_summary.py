import pytest

from awf_e2e_test import StatisticsSummary, describe


def test_describe_even_unsorted_values() -> None:
    assert describe([4, 1, 3, 2]) == StatisticsSummary(4, 2.5, 2.5, 1, 4)


def test_describe_odd_values() -> None:
    assert describe([5, 1, 3]) == StatisticsSummary(3, 3, 3, 1, 5)


def test_describe_empty() -> None:
    with pytest.raises(ValueError):
        describe([])


def test_describe_does_not_mutate_input() -> None:
    values = [4, 1, 3, 2]

    describe(values)

    assert values == [4, 1, 3, 2]


def test_describe_and_summary_are_public() -> None:
    assert describe([1]) == StatisticsSummary(1, 1, 1, 1, 1)
