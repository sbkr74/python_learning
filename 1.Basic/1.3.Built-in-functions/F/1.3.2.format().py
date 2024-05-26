# format() : it is used to define how individual values are represented
'''

The format() method in Python is used for string formatting, allowing you to insert variables or expressions 
into strings in a readable and organized manner. 
This method provides a more flexible way of formatting strings compared to the older % formatting style.
'''
# Example 1: Simple Replacement
name = "Simba"
age = 21
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)

# Example 2: Positional Arguments
formatted_string = "The {0} in {1}.".format("code", "IDE")
print(formatted_string)

# Example 3: Keyword Arguments
formatted_string = "My name is {name} and I am {age} years old.".format(name="Bob", age=25)
print(formatted_string)

# Example 4: Decimal Places
pi = 3.14159
formatted_string = "Pi to two decimal places is {:.2f}".format(pi)
print(formatted_string)

# Example 5: Comma as Thousand Separator
large_number = 1000000
formatted_string = "The large number is {:,}".format(large_number)
print(formatted_string)

# Example 6: Left, Right, and Center Alignment
left_aligned = "{:<10}".format("left")
right_aligned = "{:>10}".format("right")
center_aligned = "{:^10}".format("center")
print(left_aligned)
print(right_aligned)
print(center_aligned)

# Example 7: Combining Width, Alignment, and Number Formatting
name = "Alice"
balance = 1234.5678
formatted_string = "Name: {:<10} | Balance: ${:>10,.2f}".format(name, balance)
print(formatted_string)
