#13). strip() - this function is used to remove all the leftmost and rightmost spaces of string

# syntax:  str_name.strip()
print("   India   ".strip())
print('India'.strip())

# assigning to variables
a="a   b   c"
print(a.strip())
b=   '       dfw     '
print(b.strip())

# using with multiline string
print('''  
oxmslk
odc
'''.strip())

# lstrip() - removes only leftmost spaces
print('   India'.lstrip())
print("India   ".lstrip())

# rstrip() - remove only rightmost spaces
print('eeklf    ksdmf     '.rstrip())
print("Lucky  ".rstrip())