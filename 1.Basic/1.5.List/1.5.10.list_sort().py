items = ['Python','Objective C', 'C++','Bash Script','Java Core','Ruby','Scala','JavaScript']
items.sort()
print(items)
items.sort(reverse=True)
print(items)

# Example 2:Sorting a List of Strings by Length
words = ["banana", "pie", "Washington", "book"]
# Sort the list by the length of each string
words.sort(key=len)
print(words)  # Output: ['pie', 'book', 'banana', 'Washington']

# Example 3: Sorting a List of Tuples by the Second Element
# List of tuples
data = [(1, 3), (4, 1), (5, 2), (2, 4)]
# Sort the list by the second element of each tuple
data.sort(key=lambda x: x[1])
print(data)  # Output: [(4, 1), (5, 2), (1, 3), (2, 4)]

# Example 4 : Sorting a List of Dictionaries by a Specific Key
# List of dictionaries
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 95}
]
# Sort the list by the 'grade' key in each dictionary
students.sort(key=lambda student: student['grade'])
print(students)
# Output: [{'name': 'Bob', 'grade': 75}, {'name': 'Alice', 'grade': 88}, {'name': 'Charlie', 'grade': 95}]

# Example 5: Sorting a List of Custom Objects by an Attribute
# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} ({self.age})"

# List of Person objects
people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
]
# Sort the list by the 'age' attribute
people.sort(key=lambda person: person.age)
print(people)  # Output: [Bob (25), Alice (30), Charlie (35)]
