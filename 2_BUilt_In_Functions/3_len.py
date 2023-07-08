#3). len() - it return the length of a string i.e the no of characters presint in the string
#syntax:  len(str_name)

str1='abcdefghijklmnopqrstuvwxyz'
print(len(str1))
str2="0123456789"
print(len(str2))

# assigning to variables
a=len('India')
print(a)
b=len(str2+'@#$')
print(b)

# passing as argument
print(len('!@$%^&*'))

# it also count the no. of spaces
print(len("   "))

# for multi line string
str3='''India is my country.
All Indian are my brother and sisters.'''
print(len(str3))
