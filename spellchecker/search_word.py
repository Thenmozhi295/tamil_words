
from bloom_filter import BloomFilter
import tamil
b=BloomFilter(max_elements=2600000,error_rate=0.1)
file=open('unique_sorted_words_in_all_words_20200604-133955.txt',encoding='utf8')
b=file.read()
if 'நினைப்பினில்' in b:
   print('true')
else:
   print('false')



'''
thenmozhi@thenmozhi-Lenovo-B490:~/Documents$ time python3 search_word.py 
true

real	0m1.049s
user	0m0.603s
sys	0m0.227s
'''

