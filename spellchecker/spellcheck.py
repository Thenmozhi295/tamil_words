from bloom_filter import BloomFilter
import argparse

parser = argparse.ArgumentParser(
               description='Spell checking utility for a body of text using a list' +
    ' of correctly spelled words'
)

parser.add_argument('--num-bits', metavar='BITARRAY_LENGTH', type=int,
                    dest='num_bits',
                    help='Number of bits in the bitarray of the bloom filter')

parser.add_argument('--dictionary', metavar='DICTIONARY', type=str,
                    dest='dictionary', default='text/writerpara_unique_word.txt',
                    help='Name of file with a list of correctly spelled words')

args = parser.parse_args()

if args.num_bits:
    b = BloomFilter(k=args.num_bits)
else:
    b = BloomFilter()

with open('/home/thenmozhi/tamil_words/writerpara_unique_word.txt', 'rb') as f:
    for line in f:
        word = line.strip()
        b.add(word)
        
misspelledword = []

for words in word: 
   if words not in misspelledword: 
        misspelledword.append(words)

        print("Misspelled words:", misspelledword)
