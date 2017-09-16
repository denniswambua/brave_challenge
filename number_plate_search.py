import sys
import getopt

from kenya_plates.kenya_plates import extract_kenya_number_plates


if __name__ == "__main__":
	argv = sys.argv[1:]  # Ignore the first argument
	try:
	    opts, args = getopt.getopt(argv, "ht:")
	except getopt.GetoptError:
	    print('number_plate_search.py -t <text>')
	    sys.exit(2)
	text = ''

	for opt, arg in opts:
	    if opt == '-h':
	        print('number_plate_search.py -t <text>')
	        sys.exit()
	    elif opt == "-t":
	        text = arg
	    else:
	        assert False, "unhandled option"

	plates = extract_kenya_number_plates(text)
	print(plates)