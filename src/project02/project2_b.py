def open_file():
	input_file = ""

	while True:
		file_entry = input("\nEnter [InputFile] to extract data:")
		if len(file_entry) > 0 and file_entry[-4:] == ".txt":

			try:
				with open(file_entry, "r") as inp:
					if len(inp.read(20)) > 0:
						input_file = file_entry
						break
					else:
						print("\nError, the entered file is empty!")
			except:
				print("\nError, the entered file does not exist!")
		else:
			print("\nError, Bad file name, Enter a valid file name and format i.e. final.txt")
	return input_file


# declare year and income level as global variables
# These variables will be used by the process file function to identify the lines that;
# Contain the required year and also determine the income level
year_token = ""
income_token = ""


def process_file(file_inp):
	count = 0
	max_accum = 0
	min_accum = 0

	max_country = ""
	min_country = ""

	percentage_sum = 0

	income_level = ""

	# print("Income token:", income_token)

	if income_token == '1':
		income_level = "WB_LI"

	elif income_token == '2':
		income_level = "WB_LMI"

	elif income_token == "3":
		income_level = "WB_UMI"

	elif income_token == '4':
		income_level = "WB_HI"
	# print("income level:", income_level)

	with open("measles.txt") as f:
		for line in f:
			# Albania                                            WB_LMI  90 Europe                    1980
			if year_token in line and income_level in line:
				count += 1
				line = line.strip()

				country = line[:line.find(income_level)].strip()
				# print("Country:", country)

				end_point = line.find(income_level)
				# print("End point:", end_point)

				last_part = line[end_point + len(income_level) + 1:].strip()
				# print("Last part:", last_part)

				percent_loc = last_part.find(" ")

				percentage = int(last_part[:percent_loc].strip())
				# print("Percentage:", percentage)

				percentage_sum += percentage

				if percentage > max_accum:
					max_accum = percentage
					max_country = country

				else:
					if min_accum == 0 and percentage > min_accum:
						min_accum = percentage
						min_country = country

					elif min_accum != 0 and percentage < min_accum:
						min_accum = percentage
						min_country = country
			else:
				continue

				
	print("\nFound Matches: " + str(count))
	print("Average Percentage: " + str(round(percentage_sum / count, 1)))
	print("Lowest Percentage: Country:%s, Percentage:%s" % (min_country, str(min_accum)))
	print("Highest Percentage: Country:%s, Percentage:%s" % (max_country, str(max_accum)))
	return

def main():
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
