# function to compute amount to be billed to the customer
def bill_determiner():
	pass

# Do something forever until a break statement is encountered
while True:
	# list containing all available codes
	codes_available = ['r', 'c', 'i']

	# prompt for customer code
	cust_code = input("Enter customer code :")

	# convert customer code to lower case letters 
	# And check if its contained in the above list
	if cust_code.lower() in codes_available:
		print("Customer Code:", cust_code.lower())

	else:
		break

