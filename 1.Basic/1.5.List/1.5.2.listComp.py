itemList = ['item0','item1','item2']
itemArr = []
for i in range(3):
    itemArr.append("item"+str(i))

#list comprehension 
itemComp = ["item"+str(i) for i in range(3)]
newComp = [i.replace("item","newitem") for i in itemArr]
print(itemList)
print(itemArr)
print(itemComp)
print(newComp)