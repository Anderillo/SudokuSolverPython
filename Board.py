class Board:
	input_file = ""
	output_file = ""

	# This is what a constructor looks like in python.
	# def __init__(self):

	def initializeBoard(_input_file, _output_file):
		input_file = open(_input_file, 'r')
		output_file = open(_output_file, 'w')
		numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		board = []
		for line in input_file.readlines():
			row = []
			for char in line:
				if not char.isspace():
					if not char == ';':
						row.append(char)
					else:
						row.append(numbers)
			board.append(row)
		print board