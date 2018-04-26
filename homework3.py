import re
s = input("Что ты делаешь обычно вечером?: ")
w = input("Введите слово: ")
string = re.findall(r'%s[^\s]+%s' % (w, w),s)
print (string)
minlen = min (len(word) for word in string)
print (minlen)

