#15) ord() and chr() ufnction

# ord() - this function is used to return the ascii caode of particular charector
# Syntax:  ord("charactor")
str1="A"
print(ord(str1))
str2="a"
print(ord(str2))
# paasing as argument to function
print(ord('h'))
print(ord('9'))
# using with multiline string
print(ord('''t'''))
print()

# chr() - this function is used to return the charecter string from ascii value
# Syntax:  chr("ASCII value")
str1=65
print(chr(str1))
str2=99
print(chr(str2))
# passing with argument to function
print(chr(213))
print(chr(23))
# assignig to variable
a=chr(6)
print(a)
print(chr(0),chr(1),chr(2),chr(3),chr(4),chr(5),chr(6),chr(7))
