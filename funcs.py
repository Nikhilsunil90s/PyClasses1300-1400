def func(a,b,c , d = 90):
    print("Required Args" , a,b,c,d)


#func(10,20,30 , 40)
func(c = 90 , b = 80 , a = 50 , d = 70)
l = [1,2,3,4,5]
print(*l)# Unpacking Here
def func(*args , **kwargs): #Packing Here , * in tuple, ** in dictionary
    print(args , kwargs)


func()
func(1,2,3,4,5,6,7)
func("Hello" , 'Hey' , 'Great' , False, True , key1 = 100 , key2 = 200 , key3 = 300)

l = [4,5,6,5,10,6,5,5,30,40,2,4]
ed = {}
def func(l , ed):
    for i in l:
        ed.setdefault(i , l.count(i))
    return ed


print(func(l, ed))


print(__name__)







