# Return the biggest item in an iterable or the bigger of two or more arguments.
print(max(2,5))
print(max(5,7,6,3))
print(max([1,4,4,2,1]))

strings = ["apple", "banana", "cherry", "date"]
longest_string = max(strings, key=len)
print(longest_string)  # Output: "date"

dictionaries = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
eldest_person = max(dictionaries, key=lambda x: x["age"])
print(eldest_person)  # Output: {"name": "Bob", "age": 25}

def second_element(t):
    return t[1]

data = [(1, 3), (2, 2), (3, 1)]
max_value = max(data, key=second_element)
print(max_value)  # Output: (3, 1)


