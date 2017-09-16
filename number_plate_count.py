import sys
import getopt

from kenya_plates.kenya_plates import count_vehicle_between_number_plates


if __name__ == "__main__":
	argv = sys.argv[1:]  # Ignore the first argument
	try:
		opts, args = getopt.getopt(argv, "hf:s:")
	except getopt.GetoptError:
		print('number_plate_count.py -f <first number plate> -s <second number plate>')
		sys.exit(2)
	first = ''
	second = ''

	for opt, arg in opts:
		if opt == '-h':
			print('number_plate_count.py -f <first number plate> -s <second number plate>')
			sys.exit()
		elif opt == "-f":
			first = arg
		elif opt == "-s":
			second = arg
		else:
			assert False, "unhandled option"

	try:
		print(count_vehicle_between_number_plates(first, second))
	except Exception as e:
		print(e)
