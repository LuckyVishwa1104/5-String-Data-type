# There are differnt built in methods and function available for string
#1). count() - it return the count of a particular element
# Syntax:  str_name.count(element)
str1='banana'
print(str1.count('a'))
print(str1.count('n'))
# assigning to variables
str2="concentration"
a=str2.count('c')
b=str2.count('n')
print(a)
print(b)
# with multiline string
str3='''India is my country. All indians are my brothers.
I love my conutry.'''
# it is case sensitive
print(str3.count('I'))
# it also count the blank spaces
print("    ".count(" "))
# it return 0 for the element not present in the string
str4="""lololol"""
print(str4.count('a'))