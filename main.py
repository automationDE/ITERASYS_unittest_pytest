

def sum_two_numbers(number_1, number_2):
    return number_1 + number_2

def sub_two_numbers(number_1, number_2):
    return number_1 - number_2

def mult_two_numbers(number_1, number_2):
    return number_1 * number_2

def div_two_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return 'Its not possible to divide per zero'

def exp_two_numbers(number_1, number_2):
    return number_1 ** number_2

def calculate_circle_area(radio):
    try:
        return 3.14 * radio ** 2
    except TypeError:
        return 'Failure on calculation of Radio!'


if __name__ == '__main__':

    # Requests
    result = sum_two_numbers(5,7)
    print(f'The sum is {result}')

    result = sub_two_numbers(7,5)
    print(f'The subtration is {result}')

    result = mult_two_numbers(3,5)
    print(f'The multiplication is {result}')

    result = div_two_numbers(8,0)
    print(f'The division is {result}')

    result = exp_two_numbers(2,3)
    print(f'The exponenciation is {result}')



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
