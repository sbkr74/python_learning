import sys
# print(sys.argv[0], sys.argv[1],sys.argv[2])                       # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

print(sys.version)                                 # print python version with build date and details about the compiler and architecture
print(sys.version_info)


# Example
version_info = sys.version_info
if version_info.major < 3:
    print("Python 3 is required!")
else:
    print("Using Python 3")
    sys.exit(1)
