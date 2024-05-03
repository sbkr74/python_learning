# creating byte array
# uptill I know it is like bytes() but it is mutuable in nature
s = ['python', 'program']
asc = []
for i in s:
    for j in i:
        asc.append(ord(j))
print(asc)
b = bytearray(asc)
print(b)

b.append(109)
b.append(105)
b.append(110)
b.append(103)
print(b)