while True:
	file_entry = input("Enter File Name:")

	# Check if the entered file is the same as our easter egg
	if file_entry == "na na boo boo":
		print("NA NA BOO BOO TO YOU - You have been punk'd!")
		break
	else:
		try:
			count = 0
			# Check if the file is readable
			with open(file_entry, "r") as file_ent:

				# Iterate through all line while incrementing count
				for line in file_ent:
					count = count + 1
			print("There were %s subject lines in %s!" % (count, file_entry))
			break

		except:
			print("File cannot be opened: %s" % (file_entry))
			continue
