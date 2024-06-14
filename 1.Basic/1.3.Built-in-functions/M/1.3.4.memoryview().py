data = bytearray(b'Hello, world!')
mv = memoryview(data)
print(mv)

# Access individual elements
print(mv[0])  # Output: 72 (ASCII code for 'H')

# Slice the memory view
print(mv[0:5].tobytes())  # Output: b'Hello'

# Modify the data
mv[0] = 104  # ASCII code for 'h'
print(data)  # Output: bytearray(b'hello, world!')

