# looking to learn use of bytes()
# for now I know It is immutable array which converts integer to byte codes
# string can't be used

s = ['python', 'program']
asc = []
for i in s:
    for j in i:
        asc.append(ord(j))
print(bytes(asc))