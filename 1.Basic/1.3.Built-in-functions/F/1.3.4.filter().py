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

##############################################
# Example: Filtering High-Value Transactions
# A list of transactions (amounts in dollars)
transactions = [150, 20, 300, 50, 600, 75, 90, 1000]

# Define a function to test if a transaction is high-value (above $100)
def is_high_value(transaction):
    return transaction > 100

# Use filter() to get only high-value transactions
high_value_transactions = filter(is_high_value, transactions)

# Convert the result to a list
high_value_transactions = list(high_value_transactions)
print(high_value_transactions)

###############################################
# Example: Filtering Invalid Data from a Health Dataset
# A list of patient ages, including some invalid negative values
patient_ages = [25, 34, -5, 45, 60, -10, 29, 0]

# Define a function to check for valid ages
def is_valid_age(age):
    return age >= 0

# Use filter() to remove invalid ages
valid_patient_ages = filter(is_valid_age, patient_ages)

# Convert the result to a list
valid_patient_ages = list(valid_patient_ages)
print(valid_patient_ages)
