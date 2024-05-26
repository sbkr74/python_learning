# Define a simple function to test if a number is even
def is_even(n):
    return n % 2 == 0

# A list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to get only even numbers
even_numbers = filter(is_even, numbers)

# Convert the result to a list
even_numbers = list(even_numbers)
print(even_numbers)
