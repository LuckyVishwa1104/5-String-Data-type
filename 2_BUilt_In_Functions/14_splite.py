#15). splite() - this will separate a string by separator and return in form of list

# syntax -  str.splite()
print("India is my country.".split()) # separator is blank space
print('a,b,c,d'.split(','))  # separator is comma

# assigning to variables
a="Hello*How*Are*yOU"
print(a.split('*'))
b="lucky/nikhil/bacchi/bauwa"
print(b.split('/'))

# using multiline string
aa='''India-is-my-country'''
print(aa.split('-'))