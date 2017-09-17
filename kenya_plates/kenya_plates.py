import re
import string


KENYAN_NUMBER_PLATE_REGEX_PATTERN = "(?:[K][A-Z]{2}|GK|CD)(?:\s)?[0-9]{3}[A-Z]?"
KENYAN_NUMBER_PLATE_REGEX_PATTERN_NO_SPECIAL = "^[K][A-Z]{2}[0-9]{3}[A-Z]?$"
POST_FIX_CONSTANT = 999  # Vehicle number between postfix subsequent change



def extract_kenya_number_plates(search_text):
    """
    Extracts kenya vehicle number plates from a string
    :param search_text: string
    :return: List of found number plates
    """

    compiled_regex = re.compile(KENYAN_NUMBER_PLATE_REGEX_PATTERN, re.IGNORECASE)
    return compiled_regex.findall(search_text)


def validate_number_plate(number_plate):
    """
    Uses regex to validate kenyan number plate
    :param number_plate: string
    :return: boolean
    """

    compiled_regex = re.compile(KENYAN_NUMBER_PLATE_REGEX_PATTERN_NO_SPECIAL,
                                re.IGNORECASE)

    return True if compiled_regex.match(number_plate) else False


def get_character_index(ch):
    """
    Get character index from the alphabetic list
    :param ch:
    :return:
    """
    return string.ascii_lowercase.index(ch) + 1


def nth_number_plate(number_plate):
    """
    Gets the registration index since the begin of Kenya registrations.

    ** Assumptions and Considerations **
    -> Ignores special number plates .i.e GK001 CD001 KWTA ....
    -> First registration number `KAA001` first generation number plates. 6 characters in length.
    -> First registration number `KAA001A` second generation number plates. 7 character in length.
    -> Ignores the first letter `K` that represents  country Kenya.
    -> Each postfix change represents 999 vehicles i,e change from KAB200A to KAB200B

    :param number_plate:
    :return:
    """
    postfix_letter = None

    # Validation should ensure the number plates is either 6 or 7 in length
    if len(number_plate) == 7:

        # Get the postfix using slice
        postfix_letter = get_character_index(number_plate[-1])

    # Get the second and third character
    third_character = get_character_index(number_plate[2])
    second_character = get_character_index(number_plate[1])

    # check if its second generation and include the postfix count in plate numbers
    if postfix_letter:
        plate_numbers = int(number_plate[-4:-1])
        plate_numbers += (postfix_letter * POST_FIX_CONSTANT)
        return sum([(second_character * 26 * 26 * POST_FIX_CONSTANT), (third_character * 26 * POST_FIX_CONSTANT),
                    plate_numbers])
    else:
        plate_numbers = int(number_plate[-3:])
        return sum([(second_character * 26 * POST_FIX_CONSTANT), (third_character * POST_FIX_CONSTANT), plate_numbers])


def count_vehicle_between_number_plates(first_number_plate, second_number_plate):
    """
    Counts registered vehicles between two number plates by getting the individual
    registration index and getting the difference.

    Validation is done using regex which does not take into consideration of special
    number plates like GK... CD.. and e.t.c
    :param first_number_plate:
    :param second_number_plate:
    :return: Count of registered vehicles int
    """

    # Validate the number plates
    if not validate_number_plate(first_number_plate):
        raise Exception("Invalid first number plate {}".format(first_number_plate))

    if not validate_number_plate(second_number_plate):
        raise Exception("Invalid second number plate {}".format(second_number_plate))

    # Convert to lower case.
    first_number_plate = first_number_plate.lower()
    second_number_plate = second_number_plate.lower()

    # Return the difference between the two.
    return nth_number_plate(second_number_plate) - nth_number_plate(first_number_plate)
