# function as parameter
def sum_of_num(nums):
    return sum(nums)

def higher_order_function(f,lst):
    total = f(lst)
    return total

result = higher_order_function(sum_of_num,[1,2,3,4,5])
print(result)                                       # Output: 15

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
print(result(3))                                    # Output: 9
result = higher_order_function('cube')
print(result(3))                                    # Output: 27
result = higher_order_function('abs')
print(result(-3))                                   # Output: 3
result = higher_order_function('xyz')
# if result:
#     print(result(3))
# else:
#     print('Function not defined')

try:
    result = higher_order_function('abc')
    print(result(7))
except Exception as e:
    print("Error:",e)

# Taking both function as argument and returing a function
def apply_function_twice(func, value):
    return func(func(value))

def increment(x):
    return x + 1

result = apply_function_twice(increment, 5)
print(result)                                       # Output: 7

def create_multiplier(multiplier):
    def multiply(x):
        return x * multiplier
    return multiply

double = create_multiplier(2)
print(double(5))                                    # Output: 10
