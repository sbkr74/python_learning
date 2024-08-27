'''
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>
'''

users = {'name':'Asab', 'age':250, 'country':'Finland'}
print(users['name'])

print(users['coutry'])