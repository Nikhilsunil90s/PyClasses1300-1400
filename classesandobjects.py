# # class --- to create user defined data types
# # class is a blueprint to the objects
# # class is a set of attributes(variables) and methods(functions)

# # structures
# struct Example{
#     int i;
#     float j;
#     char k;
# }
# Example e1 , e2;
# e1.i = 90;
# e2.j = 900
# e2.k = 'K'
# e1.i, e1.j, e1.k;
# e2.i, e2.j,e2.k

# int i, j;

# class Example {
#     private:
#     int i;
#     static int j;
#     float k;
#     char arr[50];
#     public:
#     add(){

#     }
#     inpt(){
#          i = input()
#          j = input()
#          k = input()
#     }
# }

# Example E , F;
# E.i , E.j, E.k
# E.inpt()


# Example ef;


# class Example:
#     i = 0
#     j = 10
#     k = 'Hello'
#     def func1():
#         pass

#     def func2():
#         pass

class Person:
    name  = 'Max' # by default, everything is public as well as static ----- Class Variables
    age = 29
    gender = 'Male'
    def showPerson(self): # which invokes this function
        print(self.name, self.age, self.gender)
    
    def readperson(self):
        pass

print(Person.name)
Person.age = 90


P1 = Person() # invokes default constructor (a special function that creates an object and its attributes)
P2 = Person()
# print(P1.name, P2.name)
#P1.showPerson()
#P2.showPerson()
#P1.readperson()
print(P1.age, P2.age)
print(P1.name, P2.name)