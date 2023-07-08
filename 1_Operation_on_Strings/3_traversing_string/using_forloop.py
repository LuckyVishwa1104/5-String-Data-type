#3. traversing string - traversing or iterating string will print the all the character of string one by one.
# there are three ways to traverse a list

#a]. using for loop - we can travers each element of string
'''Syntax -  for var in string_name: 
                print(var)  '''
# examlple 1
str1="Lucky Vishwakarma"
for i in str1:
    print(i)

# example 2
str2='Hello_You'
for j in str2:
    print(j)

# example 3
# program to count the no. of vowels in a given string
str3=input("Enter the String : ")
v=['a','e','i','o','u']
l=[]
for p in str3:
    if p in v:
        l.append(p)
print(len(l))

# example 4
for m in 'abcdefg':
    print(m)

# example 5
# traversing a multiline string
str5='''India is my country.
I love my country'''
for t in str5:
    print(t)

