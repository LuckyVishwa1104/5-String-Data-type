# string is considered as the tupple of charracters
# using the index value we can access the element of the string
'''Syntax:
          string_name[index]'''
        
str1="Lucky Vishwakarma"
print(str1[1])
print(str1[4])
a=str1[0]
print(a)
b=str1[8]
print(b)
# empty space is also considered as the character of string
print(str1[5])

# there are multiple ways to access the elemnet of string.
#1]. using positive index:
'''Syntax :  string_name[index]  '''
str2="hello you, how are you doing!"
print(str2[2])
print(str2[5])
# special symbols are also considered as characters of string
print(str2[9])
aa=str2[5]
bb=str2[6]
print(aa)
print(bb)
print(str2[3+2])

#2]. using negative index: values are accessed from left to right
'''Syntax: string_name[-index]'''
str3='The Social Delemma'
print(str3[-1])
print(str3[-5])
a=str3[-6]
b=str3[-8]
print(a)
print(b)
print(str3[-2-7])

#3]. using slice : operator: using this we can access multiple element at a time
'''Syntax:  string_name[start:ending:strpsize]  '''
str4='India is my Country.'
print(str4[1:6])
# step size is 1 by default
print(str4[4:9])
# as stepsize is 2 value will be incremented by two
a=str4[1:11:2]
b=str4[-1:-11:-2]
print(a)
print(b)
print(str4[2:3])