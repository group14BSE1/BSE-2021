def open_file():
	pass

# declare year and income level as global variables
# These variables will be used by the process file function to identify the lines that;
# Contain the required year and also determine the income level
year_token = ""
income_token = ""
def process_file(file_inp):
	pass


def main():
	# declare these variables as global so that they can be modified by this function
	global year_token, income_token
	file_object = open_file()

	while True:
		search_year = input("Enter search [year] for data required:")
		if len(search_year) > 0 and search_year.isdigit():

			# Modify global variable year_token
			year_token = search_year
			break
		else:
			print("\nError, Enter valid input and try again!")

	while True:
		income_lv_entry = input("Enter [Income Level]:")

		# Check if a single character was entered , whether its a digit , and whether its within range
		if len(income_lv_entry) == 1 and income_lv_entry.isdigit() and 1 <= int(income_lv_entry) <= 4:

			# Modify global variable income token
			income_token = income_lv_entry
			break
		else:
			print("\nError, Enter valid input and try again!")

	# Call the process_file() function and pass file_object as a parameter
	process_file(file_object)
	return

main()