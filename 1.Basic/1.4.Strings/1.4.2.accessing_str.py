# accessing string using index
str = "python"
print(str[0])
print(str[-1])

s = input("Enter a String:")
i=0
for x in s:
    print("character at +ve index {} and -ve index {} is".format(i,i-len(s),x))
    i+=1