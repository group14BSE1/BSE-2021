fhand = open('mbox-short.txt') 
count = 0

for line in fhand:
	# List of week days
	week_days = ['Mon', 'Tue', "Wed", "Thur", "Fri", "Sat", "Sun"]

	words = line.split() 
	# print("Debug:", words)

	if len(words) == 0 or words[0] != 'From' : continue

	# check if really that day is in the list
	elif words[2] in week_days:
		print(words[2])
