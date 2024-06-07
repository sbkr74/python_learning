
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
    print("Total:",sum)

add_number()                        # calling function
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
### Function with Parameters

In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as a parameter

- Single Parameter: If our function takes a parameter we should call our function with an argument

```py
  # syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  print(function_name(argument))
```

**Example:**

```py
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Shubham'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- Two Parameter: A function may or may not have a parameter or parameters. A function may also have two or more parameters. If our function takes parameters we should call it with arguments. Let us check a function with two parameters:

```py
  # syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  print(function_name(arg1, arg2))
```

**Example:**

```py
def generate_full_name (first_name, last_name):
    space = ' '
      full_name = first_name + space + last_name
      return full_name
print('Full Name: ', generate_full_name('Shubham','Biruly'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2024, 1999))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

### Passing Arguments with Key and Value

If we pass the arguments with key and value, the order of the arguments does not matter.

```py
# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'string1', para2 = 'string2')) # the order of arguments does not matter here
```

**Example:**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Shubham', lastname = 'Biruly')
```
```py
def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
add_two_numbers(num2 = 3, num1 = 2) # Order does not matter
```

### Function with Default Parameters

Sometimes we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling the function, their default values will be used.

```py
# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
```

**Example:**

```py
def greetings (name = 'NAME'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Shubham'))
```
```py
def generate_full_name (first_name = 'first_name', last_name = 'last_name'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('Shubham','Biruly'))
```
```py
def calculate_age (birth_year,current_year = 2024):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(1999))
```
```py
def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon
```

### Function Returning a Value

Function can also return values, if a function does not have a return statement, the value of the function is None. Let us rewrite the above functions using return. From now on, we get a value from a function when we call the function and print it.

```py
def generate_full_name ():
    first_name = 'Shubham'
    last_name = 'Biruly'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
```
```py
def add_number():
    num = input("Enter numbers: ").split()
    sum = 0 
    for i in range(len(num)):
        sum+=int(num[i])
    return sum

print('Total:',add_number())       
```

- Returning a boolean:
  **Example:**

```py
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- Returning a list:
  **Example:**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```


