# 1. Identity Opertor
# is and is not
a = 10
b = 10
print(a is b)

c =11
d =10
e= d+1
print(c is e)
print(c is not d)

f1 = [1,3,4,6,7,9,4,6,8]
f2 = [2,5,6,8,9]
print(f1 is not f2) 
# 2. Membership Opertor
# in and not in
x = "Python programming from Basic to advance."
print(x)
print("to" in x)

y = [1,3,4,6,7,9,4,6,8]
print(4 in y)
print(2 in y)
print(2 not in y)