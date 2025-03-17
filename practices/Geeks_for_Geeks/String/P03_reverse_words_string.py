'''
Reverse Words in a Given String in Python
'''

string="my name is laxmi"
string_strip=string.strip()
print(" ".join(string_strip.split()[::-1]))
