# Closure: Python allows a nested function to access the outer scope of the enclosing function.
# power function
def power():
    x = int(input("Enter power of num: "))
    def sq(num):
        return num**x
    return sq

closure_result = power()
print("power:",closure_result(2))

# adder function
def adder(x):
    def adding(y):
        return x+y
    return adding

addition = adder(5)
print("adder:",addition(7))

# Access control 
def make_secure_function(func):
    secret_key = "abc123"
    
    def secure_function(key, *args, **kwargs):
        if key == secret_key:
            return func(*args, **kwargs)
        else:
            return "Unauthorized"
    
    return secure_function

def add(a, b):
    return a + b


addition = make_secure_function(add)
print(addition("abc123",7,13))
print(addition("wasd1234",7,13))
