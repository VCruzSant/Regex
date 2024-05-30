# https://docs.python.org/3/library/re.html
import re
# findall, search, sub, compile

string = 'Re test expression test'

print(re.findall(r'test', string))
print(re.search(r'test', string))
print(re.sub(r'test', 'ABC', string))
# sub count -> sub first
print(re.sub(r'test', 'ABC', string, count=1))
print()

# Compile:
regexp = re.compile(r'test')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('SUB', string))
