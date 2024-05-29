'''
update() method is used to either update existing keys or add new key-value pairs to the dictionary. 
This method can be very useful for merging dictionaries or applying multiple changes at once.
'''
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

updates = {
    'first_name':'Iam',
    'last_name':'coder',
    'age':30,
    'skills':['Python','Scala','Spark'],
    'job':['DE','DevOps','LangDev']
}
person.update(updates)
print(person)