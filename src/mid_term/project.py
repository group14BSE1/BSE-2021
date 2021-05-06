# function to compute amount to be billed to the customer
def bill_determiner(co_d, gal):

	# 5.00 and multple of gallons with 0.0005
	if co_d == "r":
		bill = 5.00 + (gal * 0.0005)
		return round(bill, 2)

	elif co_d == "c":
		# for all gallons less or equal to 4 million return 1000.00
		if gal <= 4000000:
			bill = 1000.00
			return bill

		# 1000.00 for first 4 million, then each extra 0.00025
		else:
			# for first 10 million gallons
			initial_incre = 1000.00

			# extra gallons bill
			extra = (gal - 4000000) * 0.00025

			# sum of the first 4M bill and extra gallons bill
			summed_bill = initial_incre + extra
			return round(summed_bill, 2)

	elif co_d == "i":
		if gal <= 4000000:
			bill = 1000.00
			return bill

		elif 4000000 < gal < 10000000:
			bill = 2000.00
			return bill

		elif gal > 10000000:
			# for first 10 million gallons
			initial_incre = 2000.00

			# extra gallons bill
			extra = (gal - 10000000) * 0.00025

			# sum of the first 10M bill and extra gallons bill
			summed_bill = initial_incre + extra
			return round(summed_bill, 2)






# Do something forever until a break statement is encountered
while True:
	# list containing all available codes
	codes_available = ['r', 'c', 'i']

	# prompt for customer code
	cust_code = input("\nEnter customer code :")

	# convert customer code to lower case letters 
	# And check if its contained in the above list
	if cust_code.lower() in codes_available:
		code = cust_code.lower()
		verified_start = 0
		verified_end = 0

		while True:
			start_reading_raw = input("Enter  Begining meter reading:")

			# check if the user entered something
			if len(start_reading_raw) > 0:

				# check if all entered are digits and are in the desired range
				if start_reading_raw.isdigit() and 0 < int(start_reading_raw) < 999999999:

					verified_start = int(start_reading_raw)
					break

				else:
					print("Error, Enter numeric input Otherwise enter input is in scope!")
					continue
			else:
				continue
		while True:
			end_reading_raw = input("Enter  Ending meter reading:")

			# check if the user entered something
			if len(end_reading_raw) > 0:

				# check if all entered are digits and are in the desired range
				if end_reading_raw.isdigit() and 0 < int(end_reading_raw) < 999999999: #  and int(end_reading_raw) > verified_start

					verified_end = int(end_reading_raw)
					break

				else:
					print("Error, Enter numeric input Otherwise enter input is in scope!")
					continue
			else:
				continue
		# attain a tenth of the gallons used
		used_gallons = verified_end - verified_start / 10

		# function returns a bill to be paid; It takes in the code and gallons used
		bill_2pay = bill_determiner(code, used_gallons)

		print("\nCustomer Code:", cust_code)
		print("Begining Meter reading:", verified_start)
		print("Ending Meter reading:", verified_end)
		print("Gallons of water used:", used_gallons)
		print("Amount Billed: $" + str(bill_2pay))
		continue
		
	else:
		print("\n==>: Please Enter a correct customer Code!")
		continue

