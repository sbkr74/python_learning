# single Parameter
def greet(name):
    msg = 'Hi everyone! This is '+name+'. Your Instructor in this Tutorial.'
    print(msg)

greet('Shubham')

def cubes(x):
    print("cube of",x,'is',x**3)

cubes(3)

# multiple parameter
def add(num1,num2):
    addition = num1+num2
    print(addition)

add(5,6)

def details(name,deg,des,age):
    print("Name:",name)
    print("Age:",age)
    print("Designation:",des)
    print("Degree:",deg)

details('Shubham Biruly','B.TECH(C.S.E)','Data Engineer',26)