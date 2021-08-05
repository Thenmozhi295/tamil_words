#frequency of the each word

from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("/home/thenmozhi/Documents/pandas/sramakrishnan_frequency_words.txt"))




