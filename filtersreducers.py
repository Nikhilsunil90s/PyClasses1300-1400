# Filters
#filter(callableobj , list)
li = [77,12,34,56,89,112,45,78]
oddList = []

for i in li:
    if i % 2 != 0:
        oddList.append(i)

print(oddList)
evenList = []
def checkEven(arg):
    return arg % 2 == 0

for i in li:
    if checkEven(i):
        evenList.append(i)
print(evenList)

print(list(filter(checkEven , li)))

#
li = ['Hello' , "World" , "red" , 'green' , "Orange" , 'pink' , 'purple' , 'Apple']
# to filter a l
def checkLen(arg):
    return len(arg) > 5
newL = []
for i in li:
    if checkLen(i):
        newL.append(i)
print(newL)

print(list(filter(checkLen , li)))

print(list(filter(lambda arg: arg.istitle() , li)))

# 
import functools

li = [44,22,11,77,66,55,44]

print(functools.reduce(lambda a,b : a*b , li))

li1 = ['a' , 'p' , 'p' ,'l' , 'e']
print(sum(li))# reducers
print('-'.join(li1))#reducers


#functools.reduce(callableObj - of 2 args, li)
def mysum(a,b):
    return a + b
print(functools.reduce(mysum , li1))