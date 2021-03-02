# SET OBJECTS ---- Data Structures , {} , Heterogenous
# Non array like objects ---- Unindexed, Unordered , Mutable / Immutable
# set ---- mutable
# frozenset --- immutable
# C R U D
# Create
es = {}
es = set()
print(type(es))
# Unordered, Duplicates Not Allowed
s1 = {99, 11, 88, 22, 'apple', 'a', 'p', 'p', 'l', 'e'}
print(s1)

# Read ---- no indices
# Update  ----- not allowed
# Delete
del es

# Operations ---- not allowed
# Membership
print(99 in s1)

# Slicing ---- not possible
# Comprehensions ---- not allowed

# Functions
# len()
# type()
# set()
s = {44, 11, 22, 33}
print(max(s), min(s))
print(sum(s))

# Methods
# Copies ---- Deep Copy, ShallowCopy
news = s.copy()  # shallow copy
print(news, s)
news.add(55)
print(news, s)
newd = s  # deep copy
print(newd, s)
newd.add(55)
print(newd, s)

news.clear()
print(news)

s.add(66)
print(s)
s.update([100, 200, 300])
print(s)
s.remove(11)
print(s)
print(s.pop())
print(s)

s1 = {11,44,22,33,66,55}
s2 = {100,200,300,33,11,22,400,500}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2)) # s1 - s2
print(s2.difference(s1))

# Immutable
se = {22,11,99,88,66,55,44}
fs = frozenset(se)
print(fs)
