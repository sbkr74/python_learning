#You can pass functions around as parameters
def square_number (n):
    return n * n
def cubic(f, x):
    return f(x)*x
print(cubic(square_number, 4)) # 64