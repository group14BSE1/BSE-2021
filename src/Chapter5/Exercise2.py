# Exercise 2: Write another program that prompts for a list of numbers as above and 
# at the end prints out both the maximum and minimum of the numbers instead of the 
# average. 


num_collector = list()

while True:
	number = input("\nEnter a number:")
	try:
		exact_value = float(number)

		# add a number to the list
		num_collector.append(exact_value)

	except:
		if number == "done":
			break
		else:
			print("Error, Invalid Input!")
			continue
print("Maximum:", max(num_collector))
print("Minimum:", min(num_collector))
