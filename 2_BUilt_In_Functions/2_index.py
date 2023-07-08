#2). index() - it return the index of a particular element
#Syntax:   str_name.index(element)

str1='India'
print(str1.index('I'))
print(str1.index('a'))

# assinging to variables
str2="abcdefghijklmnopqrstuvwxyz"
a=str2.index('a')
b=str2.index('z')
print(a)
print(b)

# it will return the first index only when the element is present multiple time
str3='holyyyy'
print(str3.index('y'))

# it will raise index not found error when other than string element are used
# using directly with string
print('kjhgfh'.index('j'))