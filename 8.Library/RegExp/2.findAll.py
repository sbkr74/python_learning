import re

# Finding all Matches in a String.
words = "fear, gear, tear, tire"
all_matches = re.findall(".ear",words)
print(all_matches)

# pattern #1 [Literal Match]
text = "apple banana apple grape"
matches = re.findall(r"apple", text)
print(matches)  # ['apple', 'apple']

# pattern #2 [Matching Digit]
# Example #1
sentence = "My phone number is 1234560987"
numbers = re.findall(r"\d",sentence)

'''Extracting phone numbers'''
numbers = list(map(int,numbers))
contact=0
for i in numbers:
    contact=contact*10+i
print("Contact Number: ",contact)

'''Normally extracting numbers'''
num = re.findall(r"\d+",sentence)
print(num)

# Example #2
text = "Order numbers: 0567, 4122, 210"
matches = re.findall(r"\d+", text)
print(matches)  # ['0567', '4122', '210']

