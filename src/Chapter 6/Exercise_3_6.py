def letter_counter(token, word):
	count = 0
	for letter in word:
		if letter == token:
			count = count + 1
		else:
			continue

	return count

