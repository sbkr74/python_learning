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

##############################################################
# coverting string to list without using list().
string = 'Python'
strList = [i for i in string]
print(strList)

# for generating even number and odd number
even = [num for num in range(1,21) if num%2==0]
print(even)

odd = [num for num in range(1,20) if num%2!=0]
print(odd)

# finding length of each word in a list.
def length(word):
    return len(word)

words = ['Python','Programming','from','Basic','to','advance']
word_length = [length(word) for word in words]
print(word_length) 