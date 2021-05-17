file_name = ""

while True:
	file_entry = input("Enter File Name:")
	try:
		# Check if the file is readable
		trial = open(file_entry, "r")
		trial.close()

		file_name = file_entry
		break

	except:
		print("Error, Enter a valid file name!")
		continue

# Initialize count and confidence sum
count = 0
confidence_sum = 0

# X-DSPAM-Confidence: 0.6959

with open(file_name, "r") as file_obj:
	for line in file_obj:
		if line.startswith("X-DSPAM-Confidence:"):

			# remove spaces before and those after the line i.e. end of line chracter '\n' spaces
			line = line.strip()
			count += 1
			
			# locate position of ":" , add a 1 to get position after ":"
			# slice that part up to the end of the line
			# remove spaces before and after using the strip() function to obtain the float as a string
			# Convert the float in string format to float data type using float()
			confidence = float(line[line.find(":")+1:].strip())
			confidence_sum += confidence
		else:
			continue
print("Average: " + str(confidence_sum / count))

