import re

# Finding all Matches in a String.
words = "fear, gear, tear, tire"
all_matches = re.findall(".ear",words)
print(all_matches)

# pattern #1
sentence = "My phone number is 1234560987"
numbers = re.findall(r"\d",sentence)
print(numbers)

'''Extracting phone numbers'''
num = 1

numbers = list(map(int,numbers))
k=1
for i in numbers:
    temp=i*10+numbers[k]

    print(i*10,numbers[k],temp)
    if k<len(numbers)-1:
        k+=1
    else:
        break

