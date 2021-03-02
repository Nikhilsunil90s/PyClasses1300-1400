# * ------ Pack/Unpack Operator
# Packing
# Way One
l = [22,11,44,33] # Packing
t = (100,200,300)
s = {'apple' , 'blue' , 'green' , 'orange'}
# Unpacking
# Way ONE
a,b,c,d = l # Unpack
print(a)
print(b)
print(c)
print(d)
x,y,z = t # Unpacking
print(x)
print(y)
print(z)
i,j,k,l = s
print(i , j, k, l)
# Way Two ---- use '*'
l = [22,11,44,33] # Packing
print(*l)
v = [*l] # Shallow Copy
v2 = [*t]
print(v , v2)
v[0] = 'zero'
print(v , l)
v = l







