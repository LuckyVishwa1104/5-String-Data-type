#b] using range function - using range we can traverse a string with forloop and while loop also
'''Syntax:  for i in range(len(string)):
                print(string[i]) 
                
            while i < len(string):
                print(string[i])
                i=i+1 '''

# example 1
# traversing using for loop
str1='INDIA'
for i in range(len(str1)):
    print(str1[i])

# example 2
# traversing usig while loop
str2="Good Morning"
i=0
while i<len(str2):
    print(str2[i])
    i=i+1

# example 3
for i in range(len("hello")):
    print("hello"[i])

# example 4
i=0
while i<len("world"):
    print("world"[i])
    i=i+1

# example 5
str5='holla'
for i in range(len(str5)):
    print(str5[i])
