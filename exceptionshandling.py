# Try Except
print("hello, world")
try:
    if 34 > 89:
        # "apple" / 6
        raise TypeError()
    elif 'red'  in 'reds':
        # print(x)
        raise NameError() 
    elif 34 in range(1,30):
        l = [1,2,3,4,5,6]
        # l[10]
        raise IndexError()
except TypeError:
    print("This is Type Error")
except NameError:
    print("This is Name Error")
except IndexError:
    print("This is Index Error")
else:
    print("Thats Great!")
finally:
    print("Always Executed --- Error or Not!")
print("Continued...")

def checkAge(age):
    assert age > 0
    return True

try:
    result = checkAge(90)
except AssertionError:
    print("Assertion Not Satisfied!")
else:
    print(result)


