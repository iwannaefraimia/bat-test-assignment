# bat-test-assignment

This repository contains test implementations for various functions related to Batman's tools and operations. The assignment consists of four exercises that focus on different testing techniques using pytest, including basic unit testing, fixtures, mocking, and GitHub Actions for continuous integration.

##Repository Structure

bat_functions.py - Contains the core functions to be tested.

test_bat_functions.py - Contains unit tests for the functions in bat_functions.py.

.github/workflows/pytest.yml - GitHub Actions workflow for automated testing.

##Setup

To run the tests locally, follow these steps:

1. Clone the repository: git clone https://github.com/iwannaeframia/bat-test-assignment.git
2. Navigate to the project folder: cd bat-test-assignment
3. (Optional) Create and activate a virtual environment: python -m venv venv / source venv/bin/activate  (On macOS/Linux) / venv\Scripts\activate  (On Windows)
4. Install dependencies: pip install -r requirements.txt
5. Run the tests: pytest test_bat_functions.py

###Exercise 1: Writing Basic Tests

For the following functions:

calculate_bat_power(level: int) -> int: Computes Batman's power as level * 42.

signal_strength(distance: float) -> float: Calculates the Bat-Signal strength, decreasing by 10 units per km, with a minimum of 0.

Tests Implemented:

test_calculate_bat_power: Ensures correct power calculation.

test_signal_strength: Uses pytest parameterization to test different distances.


###Exercise 2: Using Fixtures

We introduced a fixture to provide reusable data for testing Batman's vehicles.

For the function get_bat_vehicle(vehicle_name: str) -> dict which retrieves specifications for Batman's vehicles (Batmobile, Batwing, Batcycle).

Tests Implemented:

Created a pytest fixture containing Batman's vehicles.

Verified that get_bat_vehicle returns the correct specifications for known vehicles.

Ensured that the function raises an error for unknown vehicles.

###Exercise 3: Mocking External Dependencies

The function fetch_joker_info() simulates fetching Joker-related data, including a 1-second delay.

Tests Implemented:

Used pytest.monkeypatch to mock the function and return { 'mischief_level': 0, 'location': 'captured' } instead of waiting.

Verified that the mocked response was used in the test.

###Exercise 4: Continuous Integration with GitHub Actions

We set up GitHub Actions to run tests automatically:

A .github/workflows/pytest.yml workflow was created.

The workflow installs dependencies and runs pytest on push and pull_request events.

It runs on Ubuntu using Python 3.10.

##Branching Strategy

Each exercise was developed in its own branch following the naming convention:

exercise-1

exercise-2

exercise-3

exercise-4

Once completed, changes from each branch were merged into main.
This approach ensures a structured and reviewable workflow.

Conclusion

This project demonstrates fundamental testing techniques using pytest, including unit testing, fixtures, mocking, and automated testing with GitHub Actions.

