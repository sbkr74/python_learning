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

###############################################################
# Applying multiple decorator in single function

def case_mod(f):
    def top():
        func = f()
        mod = func.upper()
        return mod
    return top

def splitting(f):
    def gap():
        func = f()
        gapped = func.split()
        return gapped
    return gap

@splitting
@case_mod
def compliment():
    return 'It was good interaction.'

print(compliment())
