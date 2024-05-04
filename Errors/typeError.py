# Raised when an operation or function is applied to an object of inappropriate type.
# https://docs.python.org/3.12/library/exceptions.html#TypeError
'''
Passing arguments of the wrong type (e.g. passing a list when an int is expected) should result in a TypeError, 
but passing arguments with the wrong value (e.g. a number outside expected boundaries) should result in a ValueError.
'''
l = list(map(int,input().split()))
print(chr(l))