#8). formatting string - it is method of displaying the string by using the variables and different values.
# there are three ways of formating a string

#a). using % operator - allows to store particular type of data at specified location in string
"""%d - for integer
%s - for string
%d - for double
%f - for float"""
#syntax - "string %d string %s string"%(str,int,flot,...)
print("Hello %s"%"Lucky")
print("%s is circular. there are %d continent on earth"%("Earth",7))
# assiging to variable
a="%d * %d = %d"%(2,5,10)
print(a)
c="There are %f colours in Rainbow"%7.0
print(c)
# using with multiline string
b='''%s is my country.
All %s are my brothers and sisters.
I %s my country'''%("India","Indians","Love")
print(b)

#b). using format() method - it allows formatting through index with variables or values
# syntax: "string {0} strnig {1} string".format(vvar1,var2,...)
print("{0} is my country. All {1} are my brothers and sisters.".format("India","Indians"))
# if we assign the index it will take by default
print("Hello {} !!! {}".format("you","lucky"))
# assigning to variable
aa="{0} * {1} = {2}".format(2,5,10)
print(aa)
bb="{2} * {0} = {1}".format(5,10,2)
print(bb)
# using with multiline string
print('''Hello {0}!!!
How are {1}.
Hope you are doing {2}.'''.format("you",'you','''Well!'''))

#c). using f"_" - it allows formatting with variable name, it is most oftenly used formatting method
# syntax -  f"string {var1} string {var2} string {var3} ...."
a="Yoyo!"
print(f"Hello {a}")
b="India"
c="Indian"
print(f"""{b} is my country.
All {c} are my brother and sisters""")
# assigning to variables
aa,bb,cc=2,5,10
h=f"{aa} * {bb} = {cc}"
print(h)
v=f"{bb} * {aa} = {cc}"
print(v)
x,y,z="Lucky","You","Well"
# using with multiline string
print(f"""Hello {x} !
How are {y}.
Hope you are doing {z}?""")