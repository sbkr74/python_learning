# formatting output in python
a = 100
b = 300
c = int(a)
print("value of a is",a)
print("value of c is",c)

#Using str.format() method.
#Here curly braces {} are used as placeholder.
print('Value of a = {0} and b = {1}'.format(a,b))

#Using % operator like in C programming
print('Value of a = %d and b = %d'%(a,b))