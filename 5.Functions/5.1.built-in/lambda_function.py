# Lambda function
add = lambda a,b:a+b
print(add(3,5))                 # output: 8

square = lambda x:x**2
print(square(5))                # output: 25

# self invoking
print((lambda a,b:a+b)(2,3))    # output: 5

# using for linear equation
mult_var = lambda a,b,c:a**2-3*b+4*c
print(mult_var(5,5,3))          # output: 22

