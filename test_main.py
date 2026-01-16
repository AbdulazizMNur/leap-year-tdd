from main import is_leap_year

def test_smoke():
    assert 1 + 1 == 2

def test_div_by_4_leap():
    assert is_leap_year(2024) == True

def test_div_by_4_not_leap():
    assert is_leap_year(2025) == False

def test_div_by_100_not_leap():
    assert is_leap_year(1900) == False

def test_div_by_400_leap():
    assert is_leap_year(2000) == True