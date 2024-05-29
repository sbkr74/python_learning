person = {
    'first_name':'xyz',
    'last_name':'abc',
    'age':60,
    'country':'India',
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Somewhere in India',
        'zipcode':'888888'
    }
    }

p1 = person
p2 = person.copy()
person.popitem()
print(p1)
print(p2)