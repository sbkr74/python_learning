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

# adding items using key
person['job_title'] = 'ADE'
person['skills'].append('Java')
person['address']['city'] = 'cybercity'

# modify item in dictionary

person['first_name'] = 'Iam'
person['last_name'] = 'coder'

new_age = {'age':30}

person.update(new_age)


new_vals = [('country','Bharat'),('exp',3)]
person.update(new_vals)
print(person)
# remove item from dictionary
    # pop(key): removes item based on key
person.pop('age')

    # popitem(): remove last item from dictionary
person.popitem()

    # del : delete the item from dictionary
del person['address']

print(person)

# clear a dictionary
person.clear()

# deleting a dictionary 
del person

