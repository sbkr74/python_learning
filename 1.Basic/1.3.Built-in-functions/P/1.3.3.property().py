class Person:
    def __init__(self,name):
        self._name = name
    
    def get_name(self):
        print("Getting Name")
        return self._name
    
    def set_name(self,value):
        print("Setting Name")
        self._name = value

    def del_name(self):
        print("Deleting Name")
        del self._name

    name = property(get_name,set_name,del_name,"Name Property")

# Usage
p = Person("Alice")
print(p.name)
p.name = "Alex"
print(p.name)
del p.name