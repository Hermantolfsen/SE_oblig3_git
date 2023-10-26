#Oblig 2 Testing - Software Engineering og Testing - Herman Tolfsen
#Testing filen hvor man kjører testene
import pytest
from functions import is_leap_year


def test_leap_year_divisible_by_4():
    assert is_leap_year(2000) == True
    assert is_leap_year(2012) == True
    assert is_leap_year(2020) == True

def test_leap_year_divisible_by_100():
    assert is_leap_year(1900) == False
    assert is_leap_year(1800) == False
    assert is_leap_year(1700) == False

def test_leap_year_divisible_by_400():
    assert is_leap_year(1600) == True
    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True


def test_leap_year_not_Divisible_by_400():
    assert is_leap_year(2100) == False
    assert is_leap_year(2300) == False
    assert is_leap_year(1900) == False


def test_non_leap_year():
    assert is_leap_year(2018) == False
    assert is_leap_year(2022) == False

def test_invalid_input():
    with pytest.raises(ValueError):
        is_leap_year("invalid input")