# Progamming language as List of items
items = ['Python','Objective C', 'C++','Bash Script','Java Core','Ruby','Scala','JavaScript']
print('Items:',items)

# append() : It is used add items to List from last index
items.append('SQL')
print('Added Items:',items)         # Added Items: [......., 'SQL']
items.append('shell script')
print('more items:',items)          # more items: [........, 'SQL','shell script']

#insert(): It is used to insert the item in list whatever index you like.
items = ['Python','Objective C', 'C++','Bash Script','Java Core','Ruby','Scala','JavaScript']

# insert():
items.insert(4,'shell script')      
print(items)                        # ['Python',....,'shell script',....]
items.insert(-1,'HTML')
print(items)                        # [..........., 'HTML', 'JavaScript']

# remove(): It is used to remove item from the list
items = ['Python','Objective C', 'C++','Bash Script','Java Core','Ruby','Scala','JavaScript']

# remove():
items.remove('Ruby')
print(items)                        # ['Python', 'Objective C', 'C++', 'Bash Script', 'Java Core', 'Scala', 'JavaScript']
items.remove(items[-1])
print(items)                        # ['Python', 'Objective C', 'C++', 'Bash Script', 'Java Core', 'Scala']

# pop(): It is used to take out last item from list by default

items = ['Python','Objective C', 'C++','Bash Script','Java Core','Ruby','Scala','JavaScript']

# pop():
items.pop()
print(items)                        # ['Python', 'Objective C', 'C++', 'Bash Script', 'Java Core', 'Ruby', 'Scala']
items.pop(2)
print(items)                        # ['Python', 'Objective C', 'Bash Script', 'Java Core', 'Ruby', 'Scala']

# del

items = ['Python','Objective C', 'C++','Bash Script','Java Core','Ruby','Scala','JavaScript']

# del :
del items[-1]                       # ['Python', 'Objective C', 'C++', 'Bash Script', 'Java Core', 'Ruby', 'Scala']
print(items)
del items[0:3]
print(items)                        # ['Bash Script', 'Java Core', 'Ruby', 'Scala']

# clear() : It is used to empty the list or clean the list

items = ['Python','Objective C', 'C++','Bash Script','Java Core','Ruby','Scala','JavaScript']
items.clear()
print(items)                        # []