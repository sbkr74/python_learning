# Return the smallest item in an iterable or the smallest of two or more arguments.
print(min(2,5))
print(min(5,7,6,3))
print(min([1,4,4,2,1]))

strings = ["apple", "banana", "cherry", "date"]
shortest_string = min(strings, key=len)
print(shortest_string)  # Output: "date"

dictionaries = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
youngest_person = min(dictionaries, key=lambda x: x["age"])
print(youngest_person)  # Output: {"name": "Bob", "age": 25}

def second_element(t):
    return t[1]

data = [(1, 3), (2, 2), (3, 1)]
min_value = min(data, key=second_element)
print(min_value)  # Output: (3, 1)


