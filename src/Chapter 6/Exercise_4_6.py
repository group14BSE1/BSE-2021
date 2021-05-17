word = "banana"

count = 0

for letter in word:
	if letter == "a":
		count += 1
	else:
		continue
print("The letter [a] appears %s times!" % (str(count)))