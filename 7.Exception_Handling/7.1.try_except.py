# Basic use of try-except
try:
    print(10 + 'x')
except:
    print("operation gone wrong.")

# another example
from datetime import datetime as dt
try:
    name = input("Enter Name: ")
    year_born = input("Enter year you were born: ")
    age = dt.now().year - year_born
    print(f'You are {name} and your age is {age}.')
except:
    print('something went wrong')

'''
In above both cases, the exception block will run and we do not know exactly the problem. 
To analyze the problem, we can use the different error types with except.
'''
