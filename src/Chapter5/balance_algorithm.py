 # A dollar contains 100 cents
st_nickles = 25 # 5 cents are in a nickle
st_dimes = 25 # 10 cents are in a dime
st_quarters = 25 # 25 cents are in a quarter
st_ones = 0 # 100 cents are in one dollar
st_fives = 0 # 500 cents are in 5 dollars


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

bal = deposit_determiner(deposit)
print("Returned balance:", bal)