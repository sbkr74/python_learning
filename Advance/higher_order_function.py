# function as parameter
def sum_of_num(nums):
    return sum(nums)

def higher_order_function(f,lst):
    total = f(lst)
    return total

result = higher_order_function(sum_of_num,[1,2,3,4,5])
print(result)

# function as return value
def square(x):
    return x**2

def cube(x):
    return x**3

def abs(x):
    if x>0:
        return x
    else:
        return -(x)

def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'abs':
        return abs
    else:
        return None

result = higher_order_function('square')
print(result(3))
result = higher_order_function('cube')
print(result(3))
result = higher_order_function('abs')
print(result(-3))
result = higher_order_function('xyz')
if result:
    print(result(3))
else:
    print('Function not defined')
