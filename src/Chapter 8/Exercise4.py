romeo_handle = open('romeo.txt') 

word_collection = list()

for line in romeo_handle:
	words = line.split()

	for word in words:
		if not word in word_collection:
			word_collection.append(word)
		else:
			continue

print(sorted(word_collection))
