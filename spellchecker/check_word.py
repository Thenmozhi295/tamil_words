from tamil import utf8

string1='கோவில்'
file1=open("all_tamil_words.txt",encoding="utf8")
letters=utf8.get_letters(string1)
readfile=file1.read()

if string1 in readfile:
    print('String', string1,'Found In File')
else:
    print('String',string1,'Not Found')      