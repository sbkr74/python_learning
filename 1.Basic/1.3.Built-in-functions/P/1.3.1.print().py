print("Hello programmers to Python Basics.")
print("Hello","programmers","to Python Basics.",sep='\n')
print("Hello", end=" ")
print("World")


print("Hello", "World", sep=", ", end="!!!")
print(" How are you?")


# Open a file in write mode
with open("Data/output.txt", "w") as f:
    print("Hello, World!", file=f)
# Open a file in append mode
with open("Data/output.txt", "a") as f:
    print("Appending this line.", file=f)

# Writing to a file with explicit flushing
with open("Data/output.txt", "a") as f:
    print("appending another", file=f, flush=True)
    # Forces the data to be immediately written to the file

