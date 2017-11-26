def make_word_list(gFile):
	speech = []
	for line in gFile:
		line_list = line.split()
		for word in line_list:
			word = word.lower()
			word = word.strip(".,")
			speech.append(word)
	return speech
###############################################################
def make_unique(speech):
	unique_speech = []
	for word in speech:
		if word not in unique_speech:
			unique_speech.append(word)
	return unique_speech
#############################################################
gfile = open("get.txt","rU")
speech = make_word_list(gfile)
unique_speech = make_unique(speech)
print "len_speech = ",len(speech),"len_unique_speech = ",len(unique_speech)