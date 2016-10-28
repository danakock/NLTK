from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


s = input()
s = word_tokenize(s)

lemmatizer = WordNetLemmatizer()

lemmatized_words = []

for word in s:
	lemmatized_words.append(lemmatizer.lemmatize(word))

lemmatized_words = [w.lower() for w in lemmatized_words]

content = ["images", "mail", "apps", "people", "documents", "spreadsheets",
			"presentations", "video"]


for word in lemmatized_words:
	for c in content:
		w1 = wn.synset(word + '.n.01')
		w2 = wn.synset(c + '.n.01')
		if w1.wupsimilarity(w2) >= 0.90:
			 print(w1, w2)



