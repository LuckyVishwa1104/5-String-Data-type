#7). str() - it convert other datatype variable to string form
# syntax:  str(data-type)
# int, float, complex, bool, bin, oct,hex, list, tuple, dict, set - these datatype can be converted to string

# int, float, complex, boolian
print(str(234))
print(str(45.55))
print(str(3-7j))
print(str(True))

# assiging to variable
# bin, oct, hex
a=0b1101
b=str(a)
print(b)
c=0o3456
print(str(c))
d=str(0x12AD)
print(d)

# passing as argument
print(str([1,2,3,4,5]))
print(str((2,4,6,8)))
print({2.2,3.3,4.4,2.2})
print(str({1:1,2:4}))

a=str([2,3,4,5])
print(a[0])