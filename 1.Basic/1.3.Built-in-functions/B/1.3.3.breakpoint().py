# import pdb

# def some_function():
#     x = 5
#     y = 10
#     z = x + y

#     # Set a breakpoint
#     pdb.set_trace()

#     print("The result is:", z)

# some_function()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def some_function():
    x = 5
    y = 10
    z = x + y
    
    # Set a breakpoint here
    breakpoint()
    
    print("The result is:", z)

# Call the function
some_function()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def calculate_square_and_divide(x, y):
#     # Calculate the square of the number
#     square = x ** 2
    
#     # Set a breakpoint to inspect the variables
#     breakpoint()
    
#     # Divide the square by y
#     result = square / y
    
#     return result

# # Call the function
# result = calculate_square_and_divide(10, 2)
# print("Result:", result)


'''
You can now inspect the values of variables, execute Python code, and navigate through the code using debugger commands. For example:
Type square and press Enter to see the value of the square variable.
Type y and press Enter to see the value of the y variable.
Type c and press Enter to continue execution until the next breakpoint or until the end of the script.
Type q and press Enter to quit the debugger and terminate the script.
'''