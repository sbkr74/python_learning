class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    def get_name(self):
        print("Getting Name")
        return self._name
    
    def set_name(self,value):
        print("Setting Name")
        self._name = value

    def del_name(self):
        print("Deleting Name")
        del self._name
    
    def get_age(self):
        return self._age
    
    def set_age(self,val):
        self._age = val


    name = property(get_name,set_name,del_name,"Name Property")
    age = property(get_age,set_age,fdel=None,doc="Age property")

# Usage
p = Person("Alice",25)
print(p.name)
print(p.age)
p.name = "Alex"
p.age = 23
print(p.name)
print(p.age)
del p.name
