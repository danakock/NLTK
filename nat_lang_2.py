import nltk
from nltk.corpus import gutenberg, webtext, nps_chat, brown, reuters, inaugural, udhr, PlaintextCorpusReader, BracketParseCorpusReader, stopwords, swadesh

#nltk.corpus.gutenberg.fileids()

#emma = nltk.corpus.gutenberg.words('austen-emma.txt')
#print(len(emma))

#emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
#emma.concordance('surprize')

#gutenberg.fileids()
#emma = gutenberg.words('austen-emma.txt')

#for fileid in gutenberg.fileids():
#	num_chars = len(gutenberg.raw(fileid))
#	num_words = len(gutenberg.words(fileid))
#	num_sents = len(gutenberg.sents(fileid))
#	num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
	# average word length, average sentence length, and the number of times each vocabulary item appears in the text on average
#	print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)

#macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
#print(macbeth_sentences)
#print(macbeth_sentences[1116])	
#longest_len = max(len(s) for s in macbeth_sentences)
#l = [s for s in macbeth_sentences if len(s) == longest_len]
#print(l)

#for fileid in webtext.fileids():
#	print(fileid, webtext.raw(fileid)[:65])

#chatroom = nps_chat.posts('10-19-20s_706posts.xml')
#print(chatroom[123])

#print(brown.categories())
#print(brown.words(categories='news'))
#print(brown.words(fileids=['cg22']))
#print(brown.sents(categories=['news', 'editorial', 'reviews']))

#news_text = brown.words(categories='news')
#fdist = nltk.FreqDist(w.lower() for w in news_text)
#modals = ['can', 'could', 'may', 'might', 'must', 'will']
#for m in modals:
#	print(m + ':', fdist[m], end=' ')

#cfd = nltk.ConditionalFreqDist(
#			(genre, word)
#			for genre in brown.categories()
#			for word in brown.words(categories=genre))
#genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
#modals = ['can', 'could', 'may', 'might', 'must', 'will']
#cfd.tabulate(conditions=genres, samples=modals)

#print(reuters.fileids())
#print(reuters.categories())
#print(reuters.categories('training/9865'))
#print(reuters.categories(['training/9865', 'training/9880']))
#print(reuters.fileids('barley'))
#print(reuters.fileids(['barley', 'corn']))

#print(reuters.words('training/9865')[:14])
#print(reuters.words(['training/9865', 'training/9880']))
#print(reuters.words(categories='barley'))
#print(reuters.words(categories=['barley', 'corn']))

#print(inaugural.fileids())
#l = [fileid[:4] for fileid in inaugural.fileids()]
#print(l)

#cfd = nltk.ConditionalFreqDist(
#		(target, fileid[:4])
#		for fileid in inaugural.fileids()
#		for w in inaugural.words(fileid)
#		for target in ['america', 'citizen']
#		if w.lower().startswith(target))
#cfd.plot()

#languages = ['Chickasaw', 'English', 'German_Deutsch',
#		'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']

#cfd = nltk.ConditionalFreqDist(
#		(lang, len(word))
#		for lang in languages
#		for word in udhr.words(lang + '-Latin1'))
#cfd.plot(cumulative=True)

'''

Example	Description
fileids()	the files of the corpus
fileids([categories])	the files of the corpus corresponding to these categories
categories()	the categories of the corpus
categories([fileids])	the categories of the corpus corresponding to these files
raw()	the raw content of the corpus
raw(fileids=[f1,f2,f3])	the raw content of the specified files
raw(categories=[c1,c2])	the raw content of the specified categories
words()	the words of the whole corpus
words(fileids=[f1,f2,f3])	the words of the specified fileids
words(categories=[c1,c2])	the words of the specified categories
sents()	the sentences of the whole corpus
sents(fileids=[f1,f2,f3])	the sentences of the specified fileids
sents(categories=[c1,c2])	the sentences of the specified categories
abspath(fileid)	the location of the given file on disk
encoding(fileid)	the encoding of the file (if known)
open(fileid)	open a stream for reading the given corpus file
root	if the path to the root of locally installed corpus
readme()	the contents of the README file of the corpus'''

#raw = gutenberg.raw('burgess-busterbrown.txt')
#print(raw[1:20])
#words = gutenberg.words('burgess-busterbrown.txt')
#print(words[1:20])
#sents = gutenberg.sents('burgess-busterbrown.txt')
#print(sents[1:20])

# Load your own Corpus
#corpus_root = '/Users/dana.kock/xendo/nat_lang.py'
#wordlists = PlaintextCorpusReader(corpus_root, '.*')
#print(wordlists.fileids())

#corpus_root = r"\corpora\penntreebank\parsed\mrg\wsj"
#file_pattern = r".*/wsj_.*\.mrg" 
#ptb = BracketParseCorpusReader(corpus_root, file_pattern)
#print(ptb.fileids())
#print(len(ptb.sents()))
#print(ptb.sents(fileids='20/wsj_2013.mrg')[19])

#def plural(word):
#	if word.endswith('y'):
#		return word[:-1] + 'ies'
#	elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
#		return word + 'es'
#	elif word.endswith('an'):
#		return word[:-2] + 'en'
#	else:
#		return word + 's'

#print(plural('fairy'))
#print(plural('woman'))

# Filtering a Text: this program computes the vocabulary of a text, 
# then removes all items that occur in an existing wordlist, 
# leaving just the uncommon or mis-spelt words.

#def unusual_words(text):
#	text_vocab = set(w.lower() for w in text if w.isalpha())
#	english_vocab = set(w.lower() for w in nltk.corpus.words.words())
#	unusual = text_vocab - english_vocab
#	return sorted(unusual)

#print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')))
#print(unusual_words(nltk.corpus.nps_chat.words()))

# Corpus of stopwords, that is, high-frequency words like the, to and also that we sometimes want to filter out of a document 
# before further processing. Stopwords usually have little lexical content, and their presence in a text fails to distinguish it from other texts.
#print(stopwords.words('english'))

# define a function to compute what fraction of words in a text are not in the stopwords list
#def content_fraction(text):
#	stopwords = nltk.corpus.stopwords.words('english')
#	content = [w for w in text if w.lower() not in stopwords]
#	return len(content) / len(text) * 100

#print(content_fraction(nltk.corpus.reuters.words()))

#puzzle_letters = nltk.FreqDist('egivrvonl')
#obligatory = 'r'
#wordlist = nltk.corpus.words.words()
#l = [w for w in wordlist if len(w) >= 6
#						and obligatory in w
#						and nltk.FreqDist(w) <= puzzle_letters]
#print(len(l))

#names = nltk.corpus.names
#print(names.fileids())
#male_names = names.words('male.txt')
#female_names = names.words('female.txt')
#l = [w for w in male_names if w in female_names]
#print(l)

#cfd = nltk.ConditionalFreqDist(
#			(fileid, name[-1])
#			for fileid in names.fileids()
#			for name in names.words(fileid))
#cfd.plot()

# Pronouncing Dictionary
entries = nltk.corpus.cmudict.entries()
#print(len(entries))

#for entry in entries[42371:42379]:
#	print(entry)

#for word, pron in entries:
#	if len(pron) == 3:
#		ph1, ph2, ph3 = pron
#		if ph1 == 'P' and ph3 == 'T':
#			print(word, ph2, end=' ')

# finds all words whose pronunciation ends with a syllable sounding like nicks
#syllable = ['N', 'IHO', 'K', 'S']
#l = [word for word, pron in entries if pron[-4:] == syllable]
#print(l)

#l = [w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n']
#print(l)

#s = sorted(set(w[:2] for w, pron in entries if pron[0] == 'N' and w[0] != 'n'))
#print(s)

#def stress(pron):
#	return [char for phone in pron for char in phone if char.isdigit()]

#sl = [w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']]
#print(sl)
#l = [w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']]
#print(l)

# Find all the p-words consisting of three sounds, and group them according to their first and last sounds 
#p3 = [(pron[0]+'-'+pron[2], word)
#		for (word, pron) in entries
#		if pron[0] == 'P' and len(pron) == 3]

#cfd = nltk.ConditionalFreqDist(p3)

#for template in sorted(cfd.conditions()):
#	if len(cfd[template]) > 10:
#		words = sorted(cfd[template])
#		wordstring = ' '.join(words)
#		print(template, wordstring[:70] + '...')

#prondict = nltk.corpus.cmudict.dict()
#print(prondict['fire'])
#prondict['blog'] = [['B', 'L', 'AA1', 'G']]
#print(prondict['blog'])

# Looks up each word of the text in the pronunciation dictionary
#text = ['natural', 'language', 'processing']
#pron = [ph for w in text for ph in prondict[w][0]]
#print(pron)

#print(swadesh.fileids())
#print(swadesh.words('en'))
#fr2en = swadesh.entries(['fr', 'en'])
#print(fr2en)
#translate = dict(fr2en)
#print(translate['chien'])
#de2en = swadesh.entries(['de', 'en'])
#es2en = swadesh.entries(['es', 'en'])
#translate.update(dict(de2en))
#translate.update(dict(es2en))
#print(translate['Hund'])
#print(translate['perro'])

languages = ['en', 'de', 'nl', 'es', 'fr', 'pt', 'la']
for i in [139, 140, 141, 142]:
	print(swadesh.entries(languages)[i])