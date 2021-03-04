# Dictionaries ---- Array LIke Objects but unindexed , Mutable overall
students = ['Aman' , '2nd' , 45 , 'Male' , 'Blue']
students[4]
students = { 'Name' : 'Aman' , 'Class' : '2nd' , 'RollNo' : 45 , 'Gender' : 'Male' , 'Section' : 'Blue' } 
students['Section']

# C R U D
# Create ---- way one
# keys ---- must be of immutable type only(int, float, bool, str, tuple, ) , must be unique
# values ---- can b of any type and can repeat
#  {key:value, key:value, key:value, ....}
ed = {}
d = {33 : 'ThirtyThree' , 'Hello' : 4500 , True: 'This is Boolean' , (11,22): [100,200,300,400]}
print(type(d) , d)
# way two ---- use dict()
d1 = dict(x=100,y=200,z=300)
print(d1)

# Read --- use keys
d[33]
print(d['Hello'])
print(d[(11,22)])

# Update
d[True] = 'Updated Value'
print(d)

# Delete
del d1
del d[True]
print(d)

# Operations
# Membership Operation ---- only on keys of a dict
d = {100 : 'Hundred' , 200 : 'Two Hundred' , 400 : 'Four Hundred'}
print(100 in d)
print('Two Hundred' in d)

# Slicing --- not allowed, no indices
# Comprehensions ---- dynamic dicts
v = 'Default'
d = { k : k*k for k in range(1,6) }
print(d)

#3 x 5 x 8 ---- > '*'
l = [100,200,300,[1,2,3,4,5,[22,33,44,55]]]
#[[[''],[],[],[],[]] , [] , []]
# l = []
# al = []
# bl = []
# for z in range(3):
#     for y in range(5):
#         for x in range(8):
#             l.append('*')
#         al.append(l)
#     bl.append(al)
# print(bl)

# fl = [[['*' for k in range(8)] for j in range(5)] for i in range(3)] 
# print(fl)

# l = []
# fl = []
# fl2 = []
# for k in range(8):
#     l.append('*')
# for i in range(5):
#     fl.append(l)
# for j in range(3):
#     fl2.append(fl)
# print(fl2)

# Traversals
# Only for loop is allowed
d = { k : k*k for k in range(1,6) }
for i in d:
    print(i, d[i])

# Operations --- Method
d.copy() # shallow copy
deepd = d # Deep copy
#d.clear() to empty a dictionary
print(d.keys())
print(d.values())
print(d.items())
newd = dict.fromkeys(d)
print(newd)

d1 = {1 : 100, 2 : 200,  3 : 300}
d2 = {2 : 500, 13: 1300}
d1.update(d2)
print(d1)

print(d.pop(3))# via keys
print(d)
print(d.popitem())
print(d)
d.setdefault('key' , 'value')
print(d)
#d1[11]
print(d1.get(11))
