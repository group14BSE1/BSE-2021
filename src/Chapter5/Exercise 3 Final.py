 # A dollar contains 100 cents
st_nickles = 25 # 5 cents are in a nickle
st_dimes = 25 # 10 cents are in a dime
st_quarters = 25 # 25 cents are in a quarter
st_ones = 0 # 100 cents are in one dollar
st_fives = 0 # 500 cents are in 5 dollars

def incre_decre_determiner(value_cents, current_deposit):
	if (current_deposit - value_cents) > 0:
		return True
	elif (current_deposit - value_cents) == 0:
		return 0
	else:
		return False


def deposit_determiner(deposit):
	global st_nickles, st_dimes, st_quarters, st_ones, st_fives

def deposit_determiner(deposit):
	global st_nickles, st_dimes, st_quarters, st_ones, st_fives

	customer_deposit = deposit

	balance = 0

	while True:
		print("\n Payment due (Amount Remaining): " + str(customer_deposit) + " cents")
		paid_token = input("\nIndicate you deposit:")
		if len(paid_token) > 0:

			if paid_token == 'n':

				value_in_nickle = 5

				st_nickles += 1

				if value_in_nickle >= customer_deposit:
					balance = value_in_nickle - customer_deposit
					break
				else:
					customer_deposit = customer_deposit - value_in_nickle
					balance = customer_deposit - value_in_nickle


			elif paid_token == 'd':

				value_in_dime = 10

				st_dimes += 1

				if value_in_dime >= customer_deposit:
					balance = value_in_dime - customer_deposit
					break
				else:
					customer_deposit = customer_deposit - value_in_dime
					balance = customer_deposit - value_in_dime



			elif paid_token == 'q':

				value_in_quarter = 25

				st_quarters += 1

				if value_in_quarter >= customer_deposit:
					balance = value_in_quarter - customer_deposit
					break
				else:
					customer_deposit = customer_deposit - value_in_quarter
					balance = customer_deposit - value_in_quarter

			elif paid_token == 'o':

				value_in_ones = 100

				st_ones += 1

				if value_in_ones >= customer_deposit:
					balance = value_in_ones - customer_deposit
					break
				else:
					customer_deposit = customer_deposit - value_in_ones
					balance = customer_deposit - value_in_ones

			elif paid_token == 'f':

				value_in_fives = 500

				st_fives += 1

				if value_in_fives >= customer_deposit:
					balance = value_in_fives - customer_deposit
					break
				else:
					customer_deposit = customer_deposit - value_in_fives
					balance = customer_deposit - value_in_fives

			elif paid_token == 'c':
				break

			else:
				print("\nIllegal selection:", paid_token)


		else:
			print("\nIllegal input, please enter something!")

	return balance

#===============================================================================================================
#                               This function computes the balance
#==============================================================================================================
def balance_printer(bal):
	if bal == 0:
		print("\nPlease take the change below:\n\tNo change due.")
		return
	else:
		# Get quarters from the remaining cents 
		bal_quarters = bal // 25

		# remainder after getting quarters
		rem_quarters = bal % 25

		# Get dimes from the remaining cents
		bal_dimes = rem_quarters // 10

		# remainder after getting dimes
		rem_dimes = rem_quarters % 10

		# Get nickles from the remaining cents
		bal_nickles = rem_dimes // 5

		# remainder after getting nickles dollars
		rem_nickles = rem_dimes % 5


		print("Please take the change below:\n")
		# print(round(bal_fives), "Fives")
		# print(round(bal_ones), "Ones")
		print(round(bal_quarters), "Quarters")
		print(round(bal_dimes), "Dimes")
		print(round(bal_nickles), "Nickles")
		return







def user_input_checker():
	while True:
		# print the current stock 
		print("\nWelcome to the vending machine change maker program \n Change maker initialized.")
		print("\nStock Contains:")
		print("%d nickles" % (st_nickles))
		print("%d Dimes " % (st_dimes))
		print("%d Quarters" % (st_quarters))
		print("%d Ones" % (st_ones))
		print("%d Fives" % (st_fives))

		user_entry = input("\nEnter the purchase price (xx.xx) or 'q' to quit:")


		if len(user_entry) > 0:
			try:
				# check if the user entered numeric output
				purchase_price = float(user_entry)
				feed = round(purchase_price*100)
				if purchase_price > 0 and feed % 5 == 0:
					print("Menu for the deposits:\nn - Deposit a nickle\nd - Deposit a datetime\nq - Deposit a quarter\no - Deposit a one dollar bill\nf - Deposit a five dollar bill\nc - Cancel the purchase")
					
					dollars = feed // 100
					cents = feed % 100

					if dollars == 0:
						print("\nPayment due:" + str(cents) + "cents")
					else:
						print("\nPayment due:" + str(dollars) + " dollars and " + str(cents) + " cents")


					balance_received = deposit_determiner(feed)
					
					# print("Returned balance:", balance_received)
					balance_printer(balance_received)
					break


				else:
					print("\nIllegal price: Must be a non-negative multiple of 5 cents.")
					continue

			except:
				if user_entry == 'q':
					print("\nStock Contains:")
					print("%d nickles" % (st_nickles))
					print("%d Dimes " % (st_dimes))
					print("%d Quarters" % (st_quarters))
					print("%d Ones" % (st_ones))
					print("%d Fives" % (st_fives))
					break
				else:
					print("\nError, please enter numeric input!")
					continue

		else:
			print("\nError please enter something!")
			continue

# this function call calls the main program
user_input_checker()
