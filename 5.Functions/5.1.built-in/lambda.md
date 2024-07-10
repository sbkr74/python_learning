## Lambda Function

Lambda function is a small anonymous function without a name. It can take any number of arguments, but can only have one expression. Lambda function is similar to anonymous functions in JavaScript. We need it when we want to write an anonymous function inside another function.

### Creating a Lambda Function

To create a lambda function we use _lambda_ keyword followed by a parameter(s), followed by an expression. See the syntax and the example below. Lambda function does not use return but it explicitly returns the expression.

```py
# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))
```

**Example:**

```py
# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
```

### Lambda Function Inside Another Function

Using a lambda function inside another function.

```py
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
```
## +++++++++++++++++++++++++++++++++++++++++++
Lambda functions in Python are small anonymous functions defined using the `lambda` keyword. They can take any number of arguments, but they can only have one expression. The syntax is:

```python
lambda arguments: expression
```

Here are examples of lambda functions in basic, complex, and real-life scenarios to help you understand their use better.

### Basic Example

**Example 1: Basic Arithmetic Operation**

A simple example of a lambda function is one that performs a basic arithmetic operation, such as adding two numbers.

```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

### Complex Example

**Example 2: Sorting with Custom Key**

Lambda functions are often used in functions like `sorted()` or `sort()` where a custom sorting key is needed.

```python
# List of tuples
data = [('Alice', 25), ('Bob', 20), ('Charlie', 23)]

# Sort by age
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]
```

**Example 3: Functional Programming with Map, Filter, and Reduce**

Lambda functions are frequently used with functional programming tools like `map()`, `filter()`, and `reduce()`.

```python
from functools import reduce

# Square each number in a list using map
squared = map(lambda x: x ** 2, [1, 2, 3, 4])
print(list(squared))  # Output: [1, 4, 9, 16]

# Filter out even numbers from a list
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(list(evens))  # Output: [2, 4]

# Reduce a list to the product of its elements
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)  # Output: 24
```

### Real-Life Scenario

**Example 4: Web Development - Sorting a List of Dictionaries**

Lambda functions can be handy in web development. For example, when you have a list of dictionaries (often received from a database query), and you want to sort this list based on a particular key.

```python
users = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 23}
]

# Sort users by age
sorted_users = sorted(users, key=lambda x: x['age'])
print(sorted_users)
# Output: [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]
```

**Example 5: Data Analysis - Applying Functions to DataFrames**

In data analysis, lambda functions are often used with `pandas` DataFrames to apply a function to each row or column.

```python
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30]
})

# Apply a lambda function to each row
df['C'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
print(df)
# Output:
#    A   B   C
# 0  1  10  11
# 1  2  20  22
# 2  3  30  33
```

These examples demonstrate the versatility and utility of lambda functions in various contexts, from simple operations to more complex and real-life applications.