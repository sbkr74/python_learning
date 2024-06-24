# sorted(): It is used to create an another sorted tuple or list or dict
'''As set items can't be directly sorted'''
myList = [3,7,9,1,5,3,4,2,6,4,8]
sortedList = sorted(myList)

myTuple = (3,7,9,1,5,3,4,2,6,4,8)
sortedTuple = sorted(myTuple)

myDict = {1:'python',5:'to',3:'from',4:'Basic',2:'programming',6:'advance'}
sortedDict = sorted(myDict.values())
sortedVal = [myDict[key] for key in sorted(myDict.keys())]

# printing 
print(sortedList)
print(sortedTuple)
print(sortedDict)
print(sortedVal)