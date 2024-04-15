# still have to explore on Ternary Operator
# also known as conditional operator
# there were 2 examples of it
# example 1:
x,y = 10,20
z = 30 if x>y else 40
print(x,y,z)

#minimum of three numbers
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
min =a if a<b and a<c else b if b<c else c
print(min)
