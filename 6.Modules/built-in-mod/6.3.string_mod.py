# Basic Examples
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# Complex Example
from string import Template
template = Template('$name is $age years old and works as a $job.')
info = {
    'name':'Shubham',
    'age': 25,
    'job': 'Data Engg'
}

message = template.substitute(info)
print(message)

# Password Strength Checker
import string

def check_password_strength(password):
    has_digit = any(char in string.digits for char in password)
    has_upper = any(char in string.ascii_uppercase for char in password)
    has_lower = any(char in string.ascii_lowercase for char in password)
    has_punct = any(char in string.punctuation for char in password)
    is_long = len(password) >= 8
    return all([has_digit, has_upper, has_lower, has_punct, is_long])

password = 'Str0ng!Pass'
print(check_password_strength(password))  
passwd = input("Enter your password!\n")
print(check_password_strength(passwd))