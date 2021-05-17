# use the with key word to open file ass mb_object
with open("mbox-short.txt", "r") as mb_object:

	# Iterate over each line and remove leading spaces;
	# print contents after converting them to uppercase
	for line in mb_object:
		line = line.strip()
		print(line.upper())