#5). min() - it return the minimum element of string, it consider ascii value for comparing
# Syntax: min(string_name)

str1='abcddefghijklmnopqrstuvwxyz'
print(min(str1))
str2='0123456789'
print(min(str2))

# assining to varianles
str3='INdia'
a=min(str3)
print(a)
str4='aA'
b=min(str4)
print(b)

# passing as argument
# empty space is having least precedence
print(min("hello you"))
print(min("!@$%^&*"))
