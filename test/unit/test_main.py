import csv

import pytest

from main import sum_two_numbers, calculate_circle_area, calculate_volum_paralelogram


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
    #radio = 2
    #xpected_result = 12.56

    # Execute
    current_result = calculate_circle_area(radio)

    # Validate
    assert current_result == expected_result

#Read csv file
def read_data_csv():
    dados_csv = []
    name_file = 'C:\\Users\\railton.oliveira\\PycharmProjects\\ITERASYS_unittest_pytest\\test\\db\\mass_box.csv'
    try:
        with open(name_file, newline='') as csvfile:
            fields = csv.reader(csvfile, delimiter=',')
            next(fields)
            for line in fields:
                dados_csv.append(line)
        return dados_csv
    except FileNotFoundError:
        print(f'File not found: {name_file}')
    except Exception as fail:
        print(f'Unwaited failure: {fail}')

@pytest.mark.parametrize('id, large, comp, high, expected_result', read_data_csv())
def test_calculate_volum_paralelogram(id, large, comp, high, expected_result):
    # Configure / Prepare
    #large = 5
    #comp = 10
    #high = 2
    #expected_result = 100

    # Execute
    current_result = calculate_volum_paralelogram(int(large), int(comp), int(high))

    # Validate
    assert current_result == int(expected_result)
