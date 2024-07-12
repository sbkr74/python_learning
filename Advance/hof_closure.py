# Closure: Python allows a nested function to access the outer scope of the enclosing function.
# power function
def power():
    x = int(input("Enter power of num: "))
    def sq(num):
        return num**x
    return sq

closure_result = power()
print(f"power:",closure_result(2))

# adder function
def adder(x):
    def adding(y):
        return x+y
    return adding

addition = adder(5)
print("adder:",addition(7))