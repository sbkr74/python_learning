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

# Pattern #3 [words starting with Capital letter]
text = "aAlice went to Wonderland with Bob and Charlie"
pattern = r"[A-Z][a-z]+"
pattern1 = r"\b[A-Z][a-z]+\b"       #setting boundaries (setting first and last character)
print(re.findall(pattern, text))
print(re.findall(pattern1, text))

# Pattern #4 [Matching Words Starting ("ba")]
text = "I have ball, bat, basketball, football and boost."
pattern = r"\bba[a-z]+\b"
pattern = r"\bba\w+\b"
print(re.findall(pattern,text))

# Pattern #5 [Matching Words Ending ("ing")]
text = "I am running, jumping and swimming today."
pattern = r"\b\w+ing\b"
print(re.findall(pattern, text))

# Pattern #6 [Matching Dates (dd-mm-yyyy)]
text = "Today is 15-07-2025. Another date is 01-01-2026."
pattern = r"\b\d{2}-\d{2}-\d{4}\b"
print(re.findall(pattern, text))

# Pattern #7 [Extacting Email Address]
text = "Contact us at support@example.com or sales@myshop.org or nothing1@gov.org or aV_1g@works.co"
pattern = r"[a-z]+@[a-z]+.[a-z]+"
mod_pattern = r"[a-z0-9A-Z_.+-]+@[a-z0-9A-Z_.+-]+\.[a-z0-9A-Z_.+-]+"
print(re.findall(pattern, text))
print(re.findall(mod_pattern, text))
