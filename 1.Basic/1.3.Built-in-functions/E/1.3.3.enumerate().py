seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))

print(list(enumerate(seasons, start=1)))
x = list(enumerate(seasons,start=2))
print(x)

def enum(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1
enum(seasons,1)
print(list(enum(seasons,1)))

########################################
lang = ['Python','Java','C','C++','C#']

for index, fruit in enumerate(lang,1):
    print(index, fruit)

tasks = [
    'Write report',
    'Call John',
    'Prepare presentation',
    'Send email updates',
    'Schedule meeting with team'
]

print("To-Do List:")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

