import re
s = input("Что ты делаешь обычно вечером?: ")
string = re.findall(r'[^\s]+',s )
print (len(string))

