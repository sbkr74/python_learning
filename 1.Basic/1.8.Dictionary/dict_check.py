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

# check key is present in dictionary
print('skills' in person)
print('city' in person)

# check value in dictionary
print('India' in person.values())
print('Python' in person.values())

if 'skills' in person.keys():
    if 'Java' in person['skills']:
        print(person['skills'])