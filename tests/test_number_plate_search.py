from nose.tools import assert_equals

from kenya_plates.kenya_plates import extract_kenya_number_plates


def test_number_plate_extract():
    text = "Today morning saw a bigkbc123Asitted in kbw999 morning kkk123v GK123 KNZ980CCD143. alsoe plate with" \
           "space betweenkbq 432"
    plates = extract_kenya_number_plates(text)

    expected_list = ['kbc123A', 'kbw999', 'kkk123v', 'GK123', 'KNZ980C', 'CD143', 'kbq 432']
    assert_equals(plates, expected_list)


def test_number_plate_extract_not_found():
    text = "Today morning saw a big asd bc123Asitted in 99 morning kasgd khdf kagsui adkhs asdoakhdao"
    plates = extract_kenya_number_plates(text)

    # Expects empty list
    assert_equals(plates, [])
