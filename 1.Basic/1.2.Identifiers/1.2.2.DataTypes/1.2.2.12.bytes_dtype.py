# bytes data types store a group of byte number just like an array.
# it takes only decimal value float value can't be converted to bytes.
# and values range should be from 0 to 255.
# once created byte data type value it can't be changed.
a =[100,187,21,255,250,9,112,121,116,104]
# a = [11.1,12.9,111.77]
b = bytes(a)
print(b)