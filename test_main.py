import pytest

from main import is_leap_year


@pytest.mark.parametrize("year", [1600, 2000, 2400])
def test_years_divisible_by_400_are_leap_years(year: int) -> None:
    assert is_leap_year(year)


@pytest.mark.parametrize("year", [1700, 1800, 1900, 2100])
def test_century_years_not_divisible_by_400_are_not_leap_years(year: int) -> None:
    assert not is_leap_year(year)


@pytest.mark.parametrize("year", [1996, 2020, 2024])
def test_other_years_divisible_by_4_are_leap_years(year: int) -> None:
    assert is_leap_year(year)


@pytest.mark.parametrize("year", [1999, 2023, 2025])
def test_years_not_divisible_by_4_are_not_leap_years(year: int) -> None:
    assert not is_leap_year(year)
