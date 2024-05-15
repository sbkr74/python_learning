# startswith(): Checks if String Starts with the Specified String

string = 'python programming from Basic to Advance'
print(string.startswith('python')) # True
string = 'python programming from Basic to Advance'
print(string.startswith('Python')) # False

# endswith(): Checks if a string ends with a specified ending

string = 'python programming from Basic to Advance'
print(string.endswith('vance'))   # True
print(string.endswith('tion')) # False

# isalnum(): Checks alphanumeric character

string = 'pythonprogrammingBasictoAdvance'
print(string.isalnum()) # True

string = 'Python100days'
print(string.isalnum()) # True

string = 'python programming from Basic to Advance'
print(string.isalnum()) # False

string = 'python programming from Basic to Advance 2024'
print(string.isalnum()) # False

# isalpha(): Checks if all characters are alphabets

string = 'pythonprogramming'
print(string.isalpha()) # True
num = '100'
print(num.isalpha())      # False

# isdecimal(): Checks Decimal Characters

string = 'python programming from Basic to Advance'
print(string.find('f'))  # 19
print(string.find('to')) # 30

# isdigit(): Checks Digit Characters

string = 'hundred'
print(string.isdigit()) # False
string = '100'
print(string.isdigit())   # True

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

string = '100DaysPython'
print(string.isidentifier()) # False, because it starts with a number
string = 'python_in_100_days'
print(string.isidentifier()) # True


# islower():Checks if all alphabets in a string are lowercase

string = 'python programming from basic to advance'
print(string.islower()) # True
string = 'Python programming'
print(string.islower()) # False

# isupper(): returns if all characters are uppercase characters

string = 'python programming from Basic to Advance'
print(string.isupper()) #  False
string = 'PYTHON PROGRAMMING'
print(string.isupper()) # True


# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False
