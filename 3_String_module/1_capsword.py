# The python string module contains various functions and CONSTANT to interact with strings, to use string module function we need to import the String module.

#1). capsword() - this functions convert first character of each word of string to capital and convert remaining to small leters
# Syntax:  string.capsword(str_name)
# importing the string module
import string

str1='India is my country.'
print(string.capwords(str1))
str2="all Indians are my brothers and sisters."
print(string.capwords(str2))

# passing as parameters
print(string.capwords("lucky jitendra vishwakarma"))
print(string.capwords('''hello. how are you!'''))

# assigning to variables
a=string.capwords("applE ball cat dog elephant hen icecream")
print(a)