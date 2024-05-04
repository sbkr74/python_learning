# converts integer to unicode string.
s = ['python', 'program']
asc = []
for i in s:
    for j in i:
        asc.append(ord(j))
print(asc)
for j in asc:
    print(chr(j))
print(chr(8364))
