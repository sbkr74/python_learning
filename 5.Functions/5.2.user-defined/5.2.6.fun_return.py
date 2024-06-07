# using return keyword for returning value when called.
def add_number():
    num = input("Enter numbers: ").split()
    sum = 0 
    for i in range(len(num)):
        sum+=int(num[i])
    return sum

print('Total:',add_number())        
