# Exercise 1: Write a program which repeatedly reads numbers until the user enters 
# “done”.  Once “done” is entered, print out the total, count, and  average  of the 
# numbers. If the user enters anything other than a number, detect their mistake 
# using try and except and print an error message and skip to the next number. 

# create a list to store entered numbers
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
print("Total:", sum(num_collector))
print("Count:", len(num_collector))
print("Average:", sum(num_collector)/len(num_collector))