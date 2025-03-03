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
# enhancement in basic try-except [example 1]
try:
    print(10 + 'x')
except Exception as e:
    print(f"operation gone wrong. due to {e}.")

# handling error if you already have idea what could go wrong.
try:
    print(10 + 'x')
except TypeError:
    print("Type Error occured.")

# some cases for example 2
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2025 - year_born
    print(f'You are {name} and your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

# check for else with try-except
# also generate example for try-except with finally.