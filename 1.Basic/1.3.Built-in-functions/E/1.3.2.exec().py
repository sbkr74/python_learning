# exec(object, globals=None, locals=None, /, *, closure=None)
'''
This function supports dynamic execution of Python code. object must be either a string or a code object. 
If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs).
If it is a code object, it is simply executed. In all cases, the code that’s executed is expected to be valid as file input
'''

'''
Be aware that the nonlocal, yield, and return statements may not be used outside of function definitions 
even within the context of code passed to the exec() function. The return value is None.
'''

# Example 1: Executing a String of Code:
code = """
a = 10
b = 20
result = a + b
"""
exec(code)
print(a)
print(b)
print(result)  # Output: 30

# Example 2 : Defining a Function Dynamically:
func_code = """
def dynamic_func(x):
    return x ** 2
"""
exec(func_code)
print(dynamic_func(5))  # Output: 25

# Example 3: Modifying the Local Namespace:
local_vars = {'a': 1, 'b': 2}
exec('c = a + b', {}, local_vars)
print(local_vars['c'])  # Output: 3
print(type(local_vars))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Scenarios to use exec
'''
1. Dynamic Code Execution:
When the code to be executed is dynamically generated at runtime, exec() can be used. 
This is common in scenarios where the exact nature of the code cannot be determined until runtime.
'''
# code_snippet = input("Enter code to execute: ")
# exec(code_snippet)

'''
2. Metaprogramming:
In metaprogramming, where the program writes or manipulates code, exec() can be useful. 
This can be seen in advanced applications such as generating classes or functions dynamically based on input.
'''
class_code = """
class DynamicClass:
    def __init__(self, value):
        self.value = value
    def display(self):
        print(f'Value: {self.value}')
"""
exec(class_code)
instance = DynamicClass(10)
instance.display()  # Output: Value: 10

'''
3. Loading Configuration or Code from External Sources:

If you need to load and execute code from an external source like a configuration file, exec() can be handy. 
This is risky and should be done with caution and proper validation of the code.
'''
with open('1.Basic/1.3.Built-in-functions/E/1.3.1.eval().py', 'r') as file:
    config_code = file.read()
exec(config_code)


