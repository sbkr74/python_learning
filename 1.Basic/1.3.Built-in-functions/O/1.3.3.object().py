# declaring the object of class object
obj = object()

# printing its type
print("The type of object class object is: ")
print(type(obj))

# printing its attributes
print("The attributes of its class are: ")
print(dir(obj))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class demo():
	a = "Python"

# declaring the objects of class object
obj1 = demo()
obj2 = demo()

# checking for object equality
print("Is obj1 equal to obj2 : " + str(obj1 == obj2))

# checking for subclass
print("The Example class is a subclass of the object class? ", issubclass(demo, object)) 

# checking for object instance
print("The obj1 is a instance of the object class? ", isinstance(obj1, object))

# trying to add attribute to object
print("Default attribute: ", obj1.a)
obj1.a = "GeeksforGeeks"
print("Assigning new attribute: ", obj1.a)

