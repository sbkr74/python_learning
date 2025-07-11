import re

# Search :
# search the word or pattern in entire text or given string.
# if any word or pattern is matched it will return True.

text = "Lets learn re module together."
result = re.search("re",text)

if result:
    print("Search: Found")
else:
    print("Search: Not Found")

# Matching :
# Check for if pattern starts with 

result = re.match("Lets",text)

if result:
    print("Match: Found")
else:
    print("Match: Not Found")