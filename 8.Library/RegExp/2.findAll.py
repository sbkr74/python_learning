import re

# Finding all Matches in a String.
words = "fear, gear, tear, tire"
all_matches = re.findall(".ear",words)
print(all_matches)

# pattern #1
sentence = "My phone number is 1234560987"
numbers = re.findall(r"\d",sentence)

'''Extracting phone numbers'''
numbers = list(map(int,numbers))
contact=0
for i in numbers:
    contact=contact*10+i
print("Contact Number: ",contact)
