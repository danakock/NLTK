import nltk
from nltk.corpus import brown, inaugural, udhr

cfd = nltk.ConditionalFreqDist(
		(genre, word)
		for genre in brown.categories()
		for word in brown.words(categories=genre))

genre_word = [(genre, word)
				for genre in ['news', 'romance']
				for word in brown.words(categories=genre)]

#print(len(genre_word))
#print(genre_word[:4])
#print(genre_word[-4:])

#cfd = nltk.ConditionalFreqDist(genre_word)
#print(cfd)
#print(cfd.conditions())
#print(cfd['news'])
#print(cfd['romance'])
#print(cfd['romance'].most_common(20))
#print(cfd['romance']['could'])

#cfd = nltk.ConditionalFreqDist(
#		(target, fileid[:4])
#		for fileid in inaugural.fileids()
#		for w in inaugural.words(fileid)
#		for target in ['america', 'citizen']
#		if w.lower().startswith(target))

#cfd.plot()
#languages = ['Chickasaw', 'English', 'German_Deutsch',
	#'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']

#cfd = nltk.ConditionalFreqDist(
#		(lang, len(word))
#		for lang in languages
#		for word in udhr.words(lang + '-Latin1'))

#cfd.tabulate(conditions=['English', 'German_Deutsch'],
#			samples=range(10), cumulative=True)


#days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
#		'Friday', 'Saturday', 'Sunday']

#cfd.tabulate(conditions=['news', 'romance'], samples=days)
#cfd.plot(conditions=['news', 'romance'], samples=days)

#sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 
#		'and', 'the', 'earth', '.']

#print(list(nltk.bigrams(sent)))


# obtains all bigrams from the text of the book of Genesis, then constructs a conditional frequency distribution to record which words are most likely to follow a given word; 
#e.g., after the word living, the most likely word is creature; the generate_model() function uses this data, and a seed word, to generate random text.
#def generate_model(cfdist, word, num=15):
#	for i in range(num):
#		print(word, end =' ')
#		word = cfdist[word].max()

#text = nltk.corpus.genesis.words('english-kjv.txt')
#bigrams = nltk.bigrams(text)
#cfd = nltk.ConditionalFreqDist(bigrams)

#print(cfd['living'])
#print(generate_model(cfd, 'living'))

'''
NLTK's Conditional Frequency Distributions: commonly-used methods and idioms for defining, accessing, and visualizing a conditional frequency distribution of counters.
Example	Description
cfdist = ConditionalFreqDist(pairs)	create a conditional frequency distribution from a list of pairs
cfdist.conditions()	the conditions
cfdist[condition]	the frequency distribution for this condition
cfdist[condition][sample]	frequency for the given sample for this condition
cfdist.tabulate()	tabulate the conditional frequency distribution
cfdist.tabulate(samples, conditions)	tabulation limited to the specified samples and conditions
cfdist.plot()	graphical plot of the conditional frequency distribution
cfdist.plot(samples, conditions)	graphical plot limited to the specified samples and conditions
cfdist1 < cfdist2	test if samples in cfdist1 occur less frequently than in cfdist2'''