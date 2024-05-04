# use of complex() is to return complex number having real+imaginary number
# note: when converting from string the string must not contain whitespace around the central + or - operator.
# complex('3+2j')--->accepted
# complex('3 + 2j')---> raise ValueError.
a = '3+5.1j'
print(type(a))
print(complex(a))
a = complex(a)
print(a.real)
print(a.imag)