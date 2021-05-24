def calculator():
	num_coll = list()
	while True:
		num = input("Enter a number:")

		# check if user entered something and they are all digits
		if len(num) > 0 and num.isdigit():

			# add number to the list
			num_coll.append(int(num))

			print("Current numbers:", num_coll)

		elif len(num) > 0 and num == "done":
			break
	# compute the maximum and minimum
	print("Maximum:", max(num_coll))
	print("Minimum:", min(num_coll))
	return
calculator()

