#3) translate() - this function is used to replace a charaters with other characters
import string
# Syntax: str_name.translate(str_name.maketrans(from_chr,to_chr))

str1="banene"
a=str1.maketrans("e","a")
#print(str1)
print(str1.translate(a))
str2="aadjfaadjnad"
b=str2.maketrans("aj","AJ")
print(str2.translate(b))

# passing as parameter
print("aadomd".translate("aadomd".maketrans("ad","12")))
print("hello".translate("hello".maketrans("eo","oa")))

# assigning to variable
a="India is my Country:".translate("India is my Country:".maketrans(":","."))
print(a)
