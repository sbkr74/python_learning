To check if a specific value is present in a dictionary, you can iterate through the dictionary values and use the `in` keyword. Here are some common methods to achieve this:

### Method 1: Using a Loop

You can use a for loop to iterate through the dictionary values and check if the value is present:

```python
# Example dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "location": "NYC"
}

# Value to check
value_to_check = "NYC"

# Check if the value is in the dictionary
is_value_present = value_to_check in my_dict.values()

print(is_value_present)  # Output: True
```

### Method 2: Using List Comprehension (for more complex checks)

If you need to perform more complex checks or actions, you can use list comprehension:

```python
# Example dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "location": "NYC"
}

# Value to check
value_to_check = "NYC"

# Check if the value is in the dictionary using list comprehension
is_value_present = any(value_to_check == value for value in my_dict.values())

print(is_value_present)  # Output: True
```

### Method 3: Using the `in` Keyword Directly on `dict.values()`

You can also directly use the `in` keyword on the `values()` view of the dictionary:

```python
# Example dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "location": "NYC"
}

# Value to check
value_to_check = "NYC"

# Check if the value is in the dictionary values
is_value_present = value_to_check in my_dict.values()

print(is_value_present)  # Output: True
```

### Method 4: For Nested Dictionaries

If you have a nested dictionary, you'll need to iterate through the values recursively:

```python
def is_value_in_nested_dict(d, value_to_check):
    for v in d.values():
        if isinstance(v, dict):
            if is_value_in_nested_dict(v, value_to_check):
                return True
        elif v == value_to_check:
            return True
    return False

# Example nested dictionary
my_dict = {
    "name": "Alice",
    "details": {
        "age": 25,
        "location": "NYC"
    }
}

# Value to check
value_to_check = "NYC"

# Check if the value is in the nested dictionary
is_value_present = is_value_in_nested_dict(my_dict, value_to_check)

print(is_value_present)  # Output: True
```

These methods cover different scenarios, from simple dictionaries to nested ones, and provide a robust way to check if a value exists within a dictionary.