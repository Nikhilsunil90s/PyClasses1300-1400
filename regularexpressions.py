# regex ---> to search / Match , to find, to replace in a string
import re # only fir strings data

# match(pattern , string)
pattern = 'hey'
#str_ = 'hello, hey, this is a string'
str_ = 'Hey , this is a string again.'
#print(str_.index('hey'))
x = re.match(pattern , str_ , re.I) # matches only in the begin , I --- Ignorecase
#print(x.span())
print(x)
# search(pattern, string)
pattern = 'hey'
str_ = 'hello, this is a hey string hey'
print(re.search(pattern , str_ , re.I))
print(re.findall(pattern , str_ , re.I))

# sub()
print(re.sub(pattern , '###' , str_))

str_ = 'hello, this is a hey string hey'
pattern = 'hey'
print(str_.index(pattern) , str_.index(pattern) + len(pattern))
# Metachars ---- 
# period ( . ) ---- any single char can come in its place except '\n'
# choice ( | ) ---- 
pattern = '(gr(a|e|i|o|u)y)'
str_ = 'this string is grey in color, and gray is color, this again is griy in  or groy in color'
print(re.findall(pattern , str_))
print(re.search(pattern , str_))
# ^(beg) , $ (end)
pattern = '^th'
pattern = 'en[.]$'
str_ = 'hi that is my pen!'
print(re.search(pattern , str_))

# Repeat Meta Chars
# * ---- 0 or any number of times
# + ---- 1 or any number of times
# ? ---- 0 or 1 time
# {min , max}
pattern = 'colo(u){2,5}r'
str_ = 'this is red in colouuuuuur'
print(re.search(pattern , str_))

# Character Classes ---- no metachar holds its meaning

pattern = '[A-Z]'
pattern = '[a-z]'
pattern = '[0-9]'
pattern = '[A-Za-z0-9]'
pattern = '[AEIOU]'
pattern = '[*?+#$^.|]'
str_  = 'afshdgafsOhdgfahsgdfahsgRfdhagsfdghafsdhafsdhafshdgfahsgdfa?sd8'
print(re.search(pattern , str_))

# \w ---> [A-Za-z0-9]
# \W ---> [0-9]
email = ' \w{6,11}@{1}\w{5}.com'
str_ = 'here are 2 email ids : rediffffffffffffffff@email.com as well as example89@gmail.com'
print(re.findall(email , str_))

