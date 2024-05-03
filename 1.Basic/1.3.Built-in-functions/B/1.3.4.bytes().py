# looking to learn use of bytes()
# for now I know It is immutable array which converts integer to byte codes
# string can't be used

s = ['python', 'program']
asc = []
for i in s:
    for j in i:
        asc.append(ord(j))
print(asc)
b = bytes(asc)
print(b)

k=[100, 121, 116, 104, 111, 110, 114, 111, 103, 114, 97, 187]
b1 = bytes(k)
print(b1)