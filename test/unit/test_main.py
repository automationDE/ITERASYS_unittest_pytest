import pytest

from main import sum_two_numbers, calculate_circle_area


def test_sum_two_numbers():
    # Configure / Prepare
    number_1 = 4
    number_2 = 5
    expected_result = 9

    # Execute
    current_result = sum_two_numbers(number_1, number_2)

    # Validate
    assert current_result == expected_result


@pytest.mark.parametrize('radio,expected_result', [
                        # Values
                        (1, 3.14),   # test nr1
                        (2, 12.56),  # test nr2
                        (3, 28.26),  # test nr3
                        (4, 50.24),  # test nr4
                        ('aa', 'Failure on calculation of Radio!'),  # test nr5
                        (' ', 'Failure on calculation of Radio!'),  # test nr6
])

def test_calculate_circle_area(radio, expected_result):
    # Configure
    radio = 2
    expected_result = 12.56

    # Execute
    current_result = calculate_circle_area(radio)

    # Validate
    assert current_result == expected_result


