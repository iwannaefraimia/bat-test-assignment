import pytest
from bat_functions import calculate_bat_power, signal_strength, get_bat_vehicle

# For def calculate_bat_power
def test_calculate_bat_power():
    assert calculate_bat_power(1) == 42
    assert calculate_bat_power(2) == 84
    assert calculate_bat_power(5) == 210
    assert calculate_bat_power(0) == 0
    assert calculate_bat_power(-3) == -126  # checks negative numbers

# For def signal_strength 
@pytest.mark.parametrize("distance, expected_strength", [
    (0, 100),   # dist =  0km, the signal is 100%
    (5, 50),    # dist =  5km, the signal is 50%
    (10, 0),    # dist = 10km, the signal is 0
    (12, 0),    # dist = 12km, the signal is o
    (30, 0),    # dist = 30km, the signal is 0
])
def test_signal_strength(distance, expected_strength):
    assert signal_strength(distance) == expected_strength

@pytest.fixture
def bat_vehicles():
    """Fixture returning a dictionary of known Batman vehicles."""
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }

def test_get_bat_vehicle_known(bat_vehicles):
    """Test known vehicle specifications."""
    for vehicle, specs in bat_vehicles.items():
        assert get_bat_vehicle(vehicle) == specs

def test_get_bat_vehicle_unknown():
    """Test that an unknown vehicle raises a ValueError."""
    with pytest.raises(ValueError, match="Unknown vehicle: UnknownCar"):
        get_bat_vehicle("UnknownCar")