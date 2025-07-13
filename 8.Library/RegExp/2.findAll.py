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
# numbers = int(numbers)
for i in numbers:
    i = int(i)
    i=i*10 + (numbers[i+1])
    print(i)