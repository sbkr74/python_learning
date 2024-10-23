'''
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
'''
print(1/0)

# handling division error
try:
    print(1/0)
except ZeroDivisionError:
    print("number cannot be divided by zero")