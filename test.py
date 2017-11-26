def areAnagrames(word1,word2):
	word1_sorted = sorted(word1)
	word2_sorted = sorted(word2)
	return word1_sorted == word2_sorted:

two_words = raw_input()
two_words_list = two_words.split()
if areAnagrames(two_words_list[0],two_words_list[1]):
	print "yes"
else:
	print "no"