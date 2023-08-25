import pytest
from src.dog_age_calculator import calculate_dog_age


def test_calculate_throws_error_if_age_zero():
    with pytest.raises(ValueError) as err_msg:
        calculate_dog_age(0)
    assert str(err_msg.value) == '0 is not a valid input, age must be a number higher than 0.'


def test_calculate_throws_error_if_age_negative():
    with pytest.raises(ValueError) as err_msg:
        calculate_dog_age(-5)
    assert str(err_msg.value) == '-5 is not a valid input, age must be a number higher than 0.'


def test_calculate_if_age_1():
    assert calculate_dog_age(1) == 15
    assert calculate_dog_age(1, size='large') == 15


def test_calculate_small_dog_age():
    assert calculate_dog_age(2) == 24
    assert calculate_dog_age(6) == 40
    assert calculate_dog_age(12) == 64
    assert calculate_dog_age(16) == 80


def test_calculate_large_dog_age():
    assert calculate_dog_age(2, size='large') == 24
    assert calculate_dog_age(6, size='large') == 45
    assert calculate_dog_age(12, size='large') == 75
    assert calculate_dog_age(16, size='large') == 95
