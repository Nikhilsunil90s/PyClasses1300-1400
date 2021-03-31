class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    # def __str__(self):
    #     return f"Point({self.x} , {self.y})"
    def __repr__(self):
        return f"Point({self.x} , {self.y})"

    def __add__(self,other):
        x = self.x + other.x 
        y = self.y + other.y
        return Point(x,y)

    
    def __neg__(self):
        return Point(- self.x , - self.y)
    
    def __sub__(self,other):
        pass

    def __mul__(self,other):
        pass

    def __truediv__(self,other):
        pass

    def __floordiv__(self,other):
        if isinstance(other, Point):
            return Point(self.x // other.x , self.y // other.y)
        else:
            return Point(self.x // other , self.y // other)
        
    def __pow__(self,other):
        pass

    def __mod__(self,other):
        pass

    def __lt__(self,other):
        r1 = self.x < other.x
        r2 = self.y < other.y
        return r1 and r2
    
    def __gt__(self,other):
        pass

    def __le__(self,other):
        pass

    def __ge__(self,other):
        pass

    def __eq__(self,other):
        pass

    def __ne__(self,other):
        pass

    




P1 = Point(-19,-20)
P2 = Point(-10,90)

print(P1 , P2)
li = ['String' , 900, 8.9, False , P1]
print(li) 

P3 = P1 + P2
print(P3)

print(- P3)


print(P1 // 5)

print(P1 // P2)

print(hasattr(P1 , 'x'))
print(getattr(P2, 'y'))
li = [1,2,3,4]
print(isinstance(li, list))
#P1.z = 'Zed'
setattr(P1,'MyAttr' , 'MyValue')
print(P1.MyAttr)
#print(type(li) == '<class >')

P11 = Point(11,-88)
P12 = Point(101,-71)
print(P11 < P12)