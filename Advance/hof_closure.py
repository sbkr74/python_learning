# Closure: Python allows a nested function to access the outer scope of the enclosing function.
def power():
    x = int(input("Enter power of num: "))
    def sq(num):
        return num**x
    return sq

closure_result = power()
print(closure_result(2))

