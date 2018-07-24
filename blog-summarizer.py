from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

import csv


LANGUAGE = "english"
SENTENCES_COUNT = 5


if __name__ == "__main__":

	with open('tripotoblogs.csv', 'rU') as csvfile:
    	
   		for row in csvfile:
        		url = row
        		print(url)
    			parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    			# or for plain text files
    			# parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    			stemmer = Stemmer(LANGUAGE)

    			summarizer = Summarizer(stemmer)
    			summarizer.stop_words = get_stop_words(LANGUAGE)

    			for sentence in summarizer(parser.document, SENTENCES_COUNT):
        			print(sentence)
