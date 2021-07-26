
import re
from bs4 import BeautifulSoup
from nltk.util import ngrams
import tamil
from tamil.utf8 import get_words

htmlfile =open("/home/thenmozhi/charuonline.com/blog/index0a2a.html","r")
index=htmlfile.read()

s=BeautifulSoup(index,'html.parser')
#print(s.prettify())

text=s.get_text(strip=True)
#print(text)

text3=re.sub(r"\d","",text)

text4=re.sub(r"[a-zA-z]","",text3)

text5=re.sub(r"[•©«()..?,–]","",text4)

text6=re.sub(r"^\s+","",text5)
#print(text6)

#to print individual words

word=get_words(text6)
#print(word)

for words in word:
    print(words)

#Bigrams for the words

n=2
sentence=(text6)
unigrams=ngrams(sentence.split(),n)


for item in unigrams:
  print(item)
