
## Functions
The functions created by a user for a particular task which is not predefined or built-in system function can be said as User Defined function.

### Defining a Function

A function is a reusable block of code or programming statements designed to perform a certain task. To define or declare a function, Python provides the _def_ keyword. The following is the syntax for defining a function. The function block of code is executed only if the function is called or invoked.

### Declaring and Calling a Function

When we make a function, we call it declaring a function. When we start using the it,  we call it *calling* or *invoking* a function. Function can be declared with or without parameters.

```py
# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()
```
### Function without Parameters

Function can be declared without parameters.

**Example:**

```py
def add_number():
    num = input("Enter numbers: ").split()
    sum = 0 
    for i in range(len(num)):
        sum+=int(num[i])
    return sum

print('Total:',add_number())        # calling function in printing statement
```
```py
def skills_print():
    sk1 = 'Python'
    sk2 = 'Scala'
    sk3 = 'Spark'
    space = ' '
    print('{}{}{}{}{}'.format(sk1,space,sk2,space,sk3))
skills_print()                      # calling function
```