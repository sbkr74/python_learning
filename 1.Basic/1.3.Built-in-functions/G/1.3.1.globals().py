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


# Real-Life Scenario: Dynamic Configuration in a Financial Application
# Define global configuration parameters
interest_rate = 0.05
inflation_rate = 0.02

def update_config(param_name, value):
    global_vars = globals()
    global_vars[param_name] = value

def calculate_future_value(principal, years):
    return principal * ((1 + globals()['interest_rate']) ** years)

# Update the global interest rate
update_config('interest_rate', 0.06)

# Calculate future value with updated interest rate
future_value = calculate_future_value(1000, 5)
print(future_value)  # Output: 1338.225

# Print the current global variables
for key, value in globals().items():
    if not key.startswith("__"):
        print(f"{key}: {value}")

