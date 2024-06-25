# # Using Decorator
# class Mathutils:
#     @staticmethod
#     def add(a,b):
#         return a+b
    
# print(Mathutils.add(7,2))       # Output: 9

# Using staticmethod()
class Mathutils:
    def add(a,b):
        return a+b
    
    add = staticmethod(add)
    
print(Mathutils.add(7,3))         # Output: 10