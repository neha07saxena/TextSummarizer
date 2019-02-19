import nltk
import flask

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer

#from flask import Flask, render_template, request, session, make_response

#app = Flask(__name__)  # this just gives a name to the app
#app.secret_key = "abcde"  # Secret key is for the cookies sent over the server to get encrypted

# If you get an error uncomment this line and download the necessary libraries
#nltk.download()

text = """  The history of India includes the prehistoric settlements and societies in the Indian subcontinent; the advancement of civilisation from the Indus Valley Civilisation to the eventual blending of the Indo-Aryan culture to form the Vedic Civilisation;[1] the rise of Hinduism, Jainism and Buddhism;[2][3] the onset of a succession of powerful dynasties and empires for more than three millennia throughout various geographic areas of the Indian subcontinent, including the growth of Muslim dominions during the Medieval period intertwined with Hindu powers;[4][5] the advent of European traders and privateers, resulting in the establishment of British India; and the subsequent independence movement that led to the Partition of India and the creation of the Republic of India.[6]

Archaeological evidence of anatomically modern humans in the Indian subcontinent is estimated to be as old as 73,000-55,000 years[7] with some evidence of early hominids dating back to about 500,000 years ago.[8][9] Considered a cradle of civilisation,[10] the Indus Valley Civilisation, which spread and flourished in the north-western part of the Indian subcontinent from 3300 to 1300 BCE, was the first major civilisation in South Asia.[11] A sophisticated and technologically advanced urban culture developed in the Mature Harappan period, from 2600 to 1900 BCE.[12] This civilisation collapsed at the start of the second millennium BCE and was later followed by the Iron Age Vedic Civilisation. The era saw the composition of the Vedas, the seminal texts of Hinduism, coalesce into Janapadas (monarchical, state-level polities), and social stratification based on caste. The Later Vedic Civilisation extended over the Indo-Gangetic plain and much of the Indian subcontinent, as well as witnessed the rise of major polities known as the Mahajanapadas. In one of these kingdoms, Magadha, Gautama Buddha and Mahavira propagated their Śramaṇic philosophies during the fifth and sixth century BCE.

Most of the Indian subcontinent was conquered by the Maurya Empire during the 4th and 3rd centuries BCE. From the 3rd century BCE onwards Prakrit and Pali literature in the north and the Tamil Sangam literature in southern India started to flourish.[13][14] Wootz steel originated in south India in the 3rd century BCE and was exported to foreign countries.[15][16][17] During the Classical period, various parts of India were ruled by numerous dynasties for the next 1,500 years, among which the Gupta Empire stands out. This period, witnessing a Hindu religious and intellectual resurgence, is known as the classical or "Golden Age of India". During this period, aspects of Indian civilisation, administration, culture, and religion (Hinduism and Buddhism) spread to much of Asia, while kingdoms in southern India had maritime business links with the Middle East and the Mediterranean. Indian cultural influence spread over many parts of Southeast Asia which led to the establishment of Indianised kingdoms in Southeast Asia (Greater India).[18][19] """

stemmer = SnowballStemmer("english")
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

freqTable = dict()
for word in words:
	word = word.lower()
	if word in stopWords:
		continue

	word = stemmer.stem(word)

	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
	for word, freq in freqTable.items():
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq



sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues / len(sentenceValue))


summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
		summary += " " + sentence

print(summary)