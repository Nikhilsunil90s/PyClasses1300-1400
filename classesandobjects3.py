class Person:
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
     

    @classmethod
    def makePersonByYear(cls,name,birthyear,gender):
        from datetime import datetime
        nowObj = datetime.now()
        age = nowObj.year - birthyear
        return cls(name , age , gender)# Person()

    def __repr__(self):
        return f"Person(Name : {self.name} , Age : {self.age} , Gender : {self.gender})"
    
    @staticmethod
    def checkAge(age):
        return age > 18

    
p1 = Person("Aman" , 45 , "Male")
p2 = Person('Raman' , 54 , 'Female')
print(p1, p2)
#p3 = Person("Red" ,  , "Male") # __init__ cant be invoked here
# Factory Methods ---- classmethod ---- alternates to __init__
# Utility Methods ---- staticmethod
p3 = Person.makePersonByYear('Hello' , 1974 , 'Male')
print(p3)
print(Person.checkAge(13))