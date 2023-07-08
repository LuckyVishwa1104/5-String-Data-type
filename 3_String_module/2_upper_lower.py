# upper() and lower()
import string

#1). upper() - this function convert all the letters of a string to Upper case
# Syntax-  str.upper(Str_name)

str1='lucky vishwakarma'
print(str.upper(str1))
str2='abcdefghijklmnopqrstuvwxyz'
print(str.upper(str2))

# passing as parametrs
print(str.upper("India is my country."))
print(str.upper("all indins are my brother and sisters"))

# assigning to variables
a=str.upper('''hello you!
hope you are doing well.''')
print(a)
print()

#2). lower() - this function convert all the letter of a string to lower case
#Syntax - str.lower(str_name)

str3="LUCKY VISHWAKARMA"
print(str.lower(str3))
str4='ACBDEFGHIJKLMNOPQRSTUVWXYZ'
print(str.lower(str4))

# passing as variables
print(str.lower("maths is great."))
print(str.lower("ddlskfnv"))

# assigning to variables
b=str.lower('''vok
OSMF
MODVmsdo24@#$''')
print(b)
