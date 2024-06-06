# function without parameter
def add_number():
    num = input("Enter numbers: ").split()
    sum = 0 
    for i in range(len(num)):
        sum+=int(num[i])
    return sum

print('Total:',add_number())        # calling function

def skills_print():
    sk1 = 'Python'
    sk2 = 'Scala'
    sk3 = 'Spark'
    space = ' '
    print('{}{}{}{}{}'.format(sk1,space,sk2,space,sk3))
skills_print()                      # calling function
