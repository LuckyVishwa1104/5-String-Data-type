#12). replace() - this method will replace a specified string with particular string
# syntax -  str_name.replace("new string","old string")
print('I love my Country'.replace('Country',"India"))
print('There are 8 colours in rainbow'.replace('8','7'))
# assinging to variables
a="lucky and nikhil"
print(a.replace("nikhil",'''billionair'''))
b="one day ___"
print(b.replace('___','sure'))
# using with multiline string
str="""HII
HOw are yOu.
hoPE doing weell"""
print(str.replace('weell','well !'))