#relational operator >,>=,<=,<
a = 10 
b =20
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

print()
# With string values

s1 = 'python'
s2 = 'python'
print(s1>s2)
print(s1>=s2)
print(s1<s2)
print(s1<=s2)

print()
# With boolean values

print(True>False)
print(True>=False)
print(True<False)
print(True<=False)

print()
#extras
print(True<2)
# print(False<'xyz') can't compare bool and str
# print(10>'python') can't compare int value with str

#chaining of relational operator
print(10<20<30<50)
print(10<20<30<70<40>50)


