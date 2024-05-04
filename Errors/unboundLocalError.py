# Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
# it will raise an UnboundLocalError because the variable y is referenced before it's assigned a value within the function 
def fun():
    print("Value of Y:",y)
    y = 50
    x = int(input("enter a number:"))
    num = x
    return num
k = fun()
print(k)
