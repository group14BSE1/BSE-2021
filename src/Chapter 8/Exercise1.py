def chop(feed):
	# remove the last element
	feed.pop(-1)

	# remove first element
	feed.pop(0)
	return

def middle(feed):
	feed.pop(0)
	feed.pop(-1)

	return feed

