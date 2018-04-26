import re
s = input("Что ты делаешь обычно вечером?: ")
w = input("Введите слово: ")
string = re.findall(r'%s' % w,s)
minlen = min (len(word) for word in string)
print (minlen)
print ([word for word in string if len(word) == minlen])
