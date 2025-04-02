# Task 1
def calculate_bat_power(level):
    """
    Calculates the power of Bat-Tech based on the power level.
    Power equals level ** 2.
    """
    return level ** 2

# Task 2
def signal_strength(distance):
    """
    Calculates the strength of the Bat-Signal.
    The signal decreases linearly: max(100 - 5 * distance, 0).
    """
    return max(100 - 5 * distance, 0)
