myList = [1,3,5,7,9,11,13,15,17,19]
revList = list(reversed(myList))
print(revList)

myTuple = (1,3,5,7,9,11,13,15,17,19)
revTuple = tuple(reversed(myTuple))
print(revTuple)

try:
    mySet = {1,3,5,7,9,11,13,15,17,19}
    revSet = set(reversed(mySet))
    print(revSet)  
except TypeError as e:
    print(f"Error: {e}")                     # Error: 'set' object is not reversible    