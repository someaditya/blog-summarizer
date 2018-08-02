from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.summarizers.lex_rank import LexRankSummarizer as SummarizerLR
from sumy.summarizers.luhn import LuhnSummarizer as SummarizerLuhn
from sumy.summarizers.text_rank import TextRankSummarizer as SummarizerTR
from sumy.summarizers.edmundson import EdmundsonSummarizer as SummarizerEd

from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from  bs4  import BeautifulSoup
import urllib

import csv
import sys

reload(sys)
sys.setdefaultencoding('utf8')

LANGUAGE = "english"
SENTENCES_COUNT = 5



if __name__ == "__main__":

    list = []

    r = urllib.urlopen('https://www.tripoto.com/trip').read()
    soup = BeautifulSoup(r)
    talks= soup.find_all("a",class_='ga-link')
  

    with open('blogslist.csv', 'rU') as csvfile:
    	
        summary = " "
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
                            file = open("summary.txt","a")
                            file.write(str(sentence).encode('utf-8')+"\n") 
                            summary = summary + str(sentence).encode('utf-8')
                            print(summary)

                        with open('blogsummary.csv', 'a') as csvFile:
                            row = [url,summary]
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                            summary = " "

