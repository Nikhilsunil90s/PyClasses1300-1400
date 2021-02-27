# Tuples --- Array Like Objects, Immutable

# C R U D
# CREATE
# Way One --- use ( )
t1 = (11,22,33,44.5,66.7,88.9)
# Way Two
t2 = 'a' , 'p' , 'p' , 88 , 99, 100, 101
print(type(t1) , type(t2))
# Single Element Tuple
et = ()
st = (33,)
l = [1]
print(type(st) , type(l))

# Read ---- use indices  --- 2 way indices
# Left to Right
t = (11,22,33,44,55,66,77,88,99)
print(t[1], t[2])
# RIght To Left
print(t[-1] , t[-2])

# Update --- not allowed , Immutable
#t[0] = 'zero'

# Delete
del st
#del t[0]

# Operations
# + , *

print((1,2,3) + (9,8,7))
print(('hey' , 'hello') * 10)

print((11,22) > (1,2,3,4,5,6,7,8,9))
t = (11,22,33,44,55,66,77,88,99)
print(1 in t)

# Slicing --- beg == 0, end == len(tuple) - 1, step = 1
print(t[3::])
print(t[::2])
# To reverse a tuple
print(t[::-1])
# TRaversals
beg = 0
end = len(t)
while beg < end:
    print(t[beg])
    beg += 1
print()
for i in range(0,len(t)):
    print(t[i])
print()

for i in t:
    print(i)

# Comprehensions ---- not allowed
# FUnctions
# type()
# len()
# max()
# min()
# tuple() typecaster
l = [11,22,33,44,55]
print(l , tuple(l))
# sum()
print(sum(t))
t = (11,22,33,44,55,11,66,77,88,11,99 , 11)

print(t.count(11))
print(t.index(55))
