# Normal function
def greet():
    return "Welcome to Learning Python"

def greetings(f):
    def higher():
        func = f()
        greets = func.upper()
        return greets
    return higher
regards = greetings(greet)
print(regards())

# Decorators
def greeting(function):
    def above():
        func = function()
        return func.upper()
    return above
@greeting
def greet():
    return "Welcome to Learning Python"

print(greet())
