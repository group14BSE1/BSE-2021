
# File writer takes two parameters token (search - match string), out_file (Out put file)
def file_writer(token, out_file):
	try:
		test = open(out_file, "w")
		test.close()
	except:
		test = open(out_file, "w+")
		test.close()

	if token == "all":
		with open("measles.txt") as f:
			with open(out_file, "w") as f1:
				for line in f:
					f1.write(line)
		return

	else:
		with open("measles.txt") as f:
			with open(out_file, "w") as f1:
				for line in f:
					if token in line:
						f1.write(line)
					else:
						continue
		return
		
# The main function acts as the entry of the program
def main():
	search_token = ""
	output_file = ""

	while True:
		search_entry = input("Enter search [token] for data required:")

		# Check if user entered something , and wether the input is convertible to int
		if len(search_entry) > 0 and search_entry.isdigit():
			search_token = search_entry
			break

		elif len(search_entry) ==  0 or search_entry.lower() == "all":
			search_token = search_token.lower()
			break

		else:
			print("Error, Enter valid input and try again!\n")

	while True:
		file_entry = input("\nEnter [OutPut] File to save your data:")

		# check if something was entered and alos check wether the last 4 characters make up the ;
		# extension .txt , from the left of the filename entered we slice from the . (at index -4) to the end (:)
		if len(file_entry) > 0 and file_entry[-4:] == ".txt":
			output_file = file_entry
			break

		else:
			print("Error, Bad file name, Enter a valid file name and format i.e. final.txt\n")


	# check if the token is a year to customize search
	if search_token.isdigit():
		file_writer(search_token, output_file)

	# Either the token is "", or all to copy all contents
	else:
		file_writer("all", output_file)


main()










