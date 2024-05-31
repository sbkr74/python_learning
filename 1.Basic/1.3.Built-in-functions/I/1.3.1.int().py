# from float value
f = 17.77
print(int(f))

# from  value
s = '10'
a = int(s)
c = a * 20                      # performing calculative operation on interger item
print(c)

# from list items
myList = ['10','20','30','40']
intList = map(int,myList)
sum = 0
for item in intList:
    print(item)
    sum+=item
print(sum)