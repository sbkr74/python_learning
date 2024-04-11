# bytes data types store a group of byte number just like an array.
# it takes only decimal value float value can't be converted to bytes.
# and values range should be from 0 to 255.
a =[100,187,21,255,250,9]
# a = [11.1,12.9,111.77]
b = bytes(a)
print(b)