tup = (112,19.5,'python',False,16.5+7.11j)
print(tup)
print(type(tup))

#tuple is same as list but it is immutable
#once created we cannot modify items of tuple
print(tup[0])
print(tup[1:4])

#In tuple we cannot assign value to particular location
#Item Assignment is not supported in tuple
tup[0] = 7
print(tup[0])