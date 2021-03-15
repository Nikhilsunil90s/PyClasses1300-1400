# # Functions  ---- block of statements --- name , define , invoke/call
# def myfunc():
#     print("My Function!")
#     print("Another Statement!")

# print(type(myfunc)) # Functions are objects
# myfunc() # call operators
# # Arguments --- 4 types
# # 1. Required Arguments / Positional Args
# # 2. Default args
# # 3. Keyword Args
# def myfunc2(a,b,c = 90): # Formal Arguments
#     print(a,b,c)
#     print(a * b * c)

# myfunc2(12,13) # Actual Arguments
# myfunc2(11,22,10)
# myfunc2(c = 9, a = 1 , b = 2)# Keyword Arguments
# # 4. Variable Arguments
# def varFun(*arg , **kwarg): #packed inside a tuple here
#     print(arg , kwarg)
# #x = (100,)
# varFun()
# varFun(100)
# varFun(1,2,3,4,5,6,7,8,98)
# varFun("Hello" , False , 7.8 , 67 , [11,22,33,44] , key1 = 1000 , key2 = 2000 , key3 = 3000)

# Anonymous/Unnamed Function ----- lambda
# Single Line Functions ---- no if else/ no loops allowed
# self returning functions
#def name(args,args2,args3): 
    #body

ref = lambda x,y,z: x * y * z # Not a good practise
#ref(12,13,14)

print((lambda arg1,arg2 : arg1 * arg2)(100,200))
print((lambda arg: arg.swapcase())('Hey Strings!'))




