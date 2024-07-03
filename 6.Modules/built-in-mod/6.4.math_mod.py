# So Basically Module is the collection of function,variable and classes
import math
print(dir(math))
print(math.sqrt(16))
print(math.pow(2,4))
print(math.pi)
print(math.e)


# +++++++++++++++++++++++++++++++++++++++++++++++++++
import cmath
print(cmath.sqrt(-1))
print(cmath.sqrt(4+9j))

print(cmath.phase(4+9j))
# +++++++++++++++++++++++++++++++++++++++++++++++++++


def decibels(intensity):
    return 10 * math.log10(intensity)

print(decibels(1000)) 
print(decibels(1000000)) 