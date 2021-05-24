def mail_manager():

	file_coll = open("mbox-short.txt")

	count = 0

	for line in file_coll:
		if len(line) > 0 and line.startswith("From"):
			count += 1

			# break line into a list basing on spaces
			spread = line.split()

			# get sender  at index 1
			print(spread[1])
			
		else:
			continue
	return count
number = mail_manager()

print("There were %s lines beginning with [From] as the first word" % (number))