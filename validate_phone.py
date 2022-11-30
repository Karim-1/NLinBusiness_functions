import csv
import re

from phonenumbers import carrier, parse, is_possible_number, is_valid_number
from phonenumbers.phonenumberutil import number_type

def validate_phone(number_string):
    """_summary_

    Args:
        number_string (string): phone number 

    Returns:
        is_valid_nr (bool)
        number (string): converted phone number
    """
    # check for '06' nrs, phonenumbers package doesnt recognise nr without area code
    if number_string.startswith('06'):
        number_string = number_string.removeprefix('06')
        number_string = '+316'+number_string

   
    # check if string contains letters
    if re.search('[a-zA-Z]', number_string):
        print(f'Error: {number_string} contains letters, is not a valid phone number.')
        return False, number_string

    # check if phonenumbers package recognises number
    parsed_nr = parse(number_string)
    is_valid_nr = is_valid_number(parsed_nr)
    is_possible_nr = is_possible_number(parsed_nr)

    if not is_valid_nr and is_possible_nr:
        print(f'Error: {number_string} is not a valid phone number')
        print(is_valid_nr, is_possible_nr)

    # format number string
    number = number_string.replace('+', '00')

    return is_valid_nr, number



if __name__ == '__main__':
    file = 'dummy_phonenumbers.csv'
    with open(file, newline='') as f:
        reader = csv.reader(f)
        numbers_lists = list(reader)
        numbers = [item for sublist in numbers_lists for item in sublist]

    for nr in numbers:
        validate_phone(nr)