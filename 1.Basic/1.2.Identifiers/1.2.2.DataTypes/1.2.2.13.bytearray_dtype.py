#bytearray is exactly same as bytes data type except its elements can be modified.
a = [100,121,144,251]
b = bytearray(a)
print(type(b))
print(b)
# for i in b:
#     print(i)

b[1] = 155
print(b)

# for i in b:
#     print(i)