# Basic Usage
'''
The globals() function can be particularly useful for:
    1. Accessing global variables dynamically.
    2. Inspecting global variables and their values.
    3. Modifying global variables from within functions.
'''
# Example 1: Accessing Global Variables
# Define some global variables
x = 10
y = 20

# Use globals() to access the global variables
global_vars = globals()
print(global_vars['x'])  # Output: 10
print(global_vars['y'])  # Output: 20

def access():
    gbl_vars = globals()
    print(gbl_vars['x'])
    print(gbl_vars['y'])

access()

# Example 2: Modifying Global Variables within a Function
# Global variable
counter = 0

def increment_counter():
    global_vars = globals()
    global_vars['counter'] += 1

increment_counter()
print(counter)  # Output: 1

# Example 3: Dynamically Creating and Accessing Global Variables
# Define some variables
a = 5
b = 15

# Create a new global variable dynamically
globals()['c'] = a + b
print(c)  # Output: 20
