#prompt the user for input
hours = input("Hours:")

# prompt for the rate
rate = input("Rate:")

def computenpay(hr, rt):
	# check if the required input is fed in
	try:
		h_rs = float(hr)
		ra_te = float(rt)

		if h_rs <= 40:
			pay = h_rs*ra_te
			print("Pay:", pay)
		else:
			full_pay = h_rs*ra_te

			overtime_pay = ((h_rs-40) * rate) / 2

			final_pay = full_pay + overtime_pay
			print("Pay:", final_pay)
	except:
		print("Error, please enter numeric input")

# check if they entered something
if len(hours) > 0 and len(rate) > 0:
	# call the computepay function with hours and the rate as input
	computenpay(hours, rate)
else:
	print("Error please supply all the required input!")