import pytest
from bat_functions import calculate_bat_power, signal_strength

# Task 1: For def calculate_bat_power
def test_calculate_bat_power():
    assert calculate_bat_power(1) == 42
    assert calculate_bat_power(2) == 84
    assert calculate_bat_power(5) == 210
    assert calculate_bat_power(0) == 0
    assert calculate_bat_power(-3) == -126  # checks negative numbers

# Task 2: For def signal_strength 
@pytest.mark.parametrize("distance, expected_strength", [
    (0, 100),   # dist =  0km, the signal is 100%
    (5, 50),    # dist =  5km, the signal is 50%
    (10, 0),    # dist = 10km, the signal is 0
    (12, 0),    # dist = 12km, the signal is o
    (30, 0),    # dist = 30km, the signal is 0
])
def test_signal_strength(distance, expected_strength):
    assert signal_strength(distance) == expected_strength