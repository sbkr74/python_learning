# dir() shows all function that can used it variable or datatype passed as arguement
print(dir())
print()
print(dir(str))

class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']


s = Shape()
print()
print(dir(s))
