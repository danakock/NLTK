from nltk import bigrams
from nltk.book import *

def lexical_diversity(text):
	return len(set(text)) / len(text)

def percentage(count, total):
	return 100 * count / total

v = set(text5)
l = [w for w in v if len(w) == 4]
print(len(l))

#saying = ['After', 'all', 'is', 'said', 'and', 'done',
 #       'more', 'is', 'said', 'than', 'done']
#tokens = set(saying)
#print(tokens)
#tokens = sorted(tokens)
#print(tokens)
#print(tokens[-2:])

#fdist1 = FreqDist(text6)
#print(fdist1)
#print(fdist1.most_common(50))
#print(fdist1['whale'])
#fdist1.plot(50, cumulative=True)
#print(fdist1.hapaxes())

#V = set(text1)
#long_words = [w for w in V if len(w) > 15]
#print(sorted(long_words))

#fdist5 = FreqDist(text5)
#print(sorted (w for w in set(fdist5) if len(w) > 7 and fdist5[w] > 7))

#print(list(bigrams(['more', 'is', 'said', 'than', 'done'])))

#print(text4.collocations())
#print(text8.collocations())

l = [len(w) for w in text1]
fdist = FreqDist(l)
#print(fdist)
#print(fdist.most_common())
#print(fdist.max())
#print(fdist[3])
#print(fdist.freq(3))

#print(sorted(w for w in set(text7) if '-' in w and 'index' in w))

# eliminate upper/lower duplicates and non-letters
len(set(word.lower() for word in text1 if word.isalpha()))

tricky = sorted(w for w in set(text2) if 'cie' in w or 'cei' in w)
for word in tricky:
	print(word, end=' ')
'''
Frequency Distribution
Example	Description
fdist = FreqDist(samples)	create a frequency distribution containing the given samples
fdist[sample] += 1	increment the count for this sample
fdist['monstrous']	count of the number of times a given sample occurred
fdist.freq('monstrous')	frequency of a given sample
fdist.N()	total number of samples
fdist.most_common(n)	the n most common samples and their frequencies
for sample in fdist:	iterate over the samples
fdist.max()	sample with the greatest count
fdist.tabulate()	tabulate the frequency distribution
fdist.plot()	graphical plot of the frequency distribution
fdist.plot(cumulative=True)	cumulative plot of the frequency distribution
fdist1 |= fdist2	update fdist1 with counts from fdist2
fdist1 < fdist2	test if samples in fdist1 occur less frequently than in fdist2'''

'''
Word Comparison Operators
s.startswith(t)	test if s starts with t
s.endswith(t)	test if s ends with t
t in s	test if t is a substring of s
s.islower()	test if s contains cased characters and all are lowercase
s.isupper()	test if s contains cased characters and all are uppercase
s.isalpha()	test if s is non-empty and all characters in s are alphabetic
s.isalnum()	test if s is non-empty and all characters in s are alphanumeric
s.isdigit()	test if s is non-empty and all characters in s are digits
s.istitle()	test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals)'''