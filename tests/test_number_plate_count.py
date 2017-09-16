from nose.tools import assert_raises
from nose.tools import assert_equals

from kenya_plates.kenya_plates import count_vehicle_between_number_plates


def test_number_plate_count():
    first = "kbb632a"
    second = "kbb632e"

    result = count_vehicle_between_number_plates(first, second)

    assert_equals(result, 3996)


def test_number_plate_count_validation():
    invalid_numbers = "kca1221"
    second = "kaa001b"

    assert_raises(Exception, count_vehicle_between_number_plates,
		          invalid_numbers, second)

    first_number = "kca122i"
    invalid_second = "kca12qw"

    assert_raises(Exception, count_vehicle_between_number_plates,
		          first_number, invalid_second)


def test_number_plate_count_semi_major_change():
    first = "kaa001a"
    second = "kab001a"

    result = count_vehicle_between_number_plates(first, second)

    assert_equals(result, 25974)


def test_number_plate_count_major_change():
    first = "kaa001a"
    second = "kba001a"

    result = count_vehicle_between_number_plates(first, second)

    assert_equals(result, 675324)


def test_number_plate_count_same_version():
    first = "kbw123j"
    second = "kbw124j"

    result = count_vehicle_between_number_plates(first, second)

    assert_equals(result, 1)

    first = "kcb001a"
    second = "kcb101a"

    result = count_vehicle_between_number_plates(first, second)

    assert_equals(result, 100)


def test_number_plate_count_first_generation():
    first = "kaa001"
    second = "kaa002"

    result = count_vehicle_between_number_plates(first, second)

    assert_equals(result, 1)

    first = "kaa001"
    second = "kzz999"

    result = count_vehicle_between_number_plates(first, second)

    assert_equals(result, 675323)


def test_number_plate_count_first_n_second_generation():
    first = "kzz999"
    second = "kaa001a"

    result = count_vehicle_between_number_plates(first, second)

    assert_equals(result, 1)

    first = "kzz999"
    second = "kaa051b"

    result = count_vehicle_between_number_plates(first, second)

    assert_equals(result, 1050)
