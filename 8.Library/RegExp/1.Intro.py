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

# Special Symbols
# (.) - any single character
if re.search("c.t","I have a cat. But also cut my finger."):
    print("(.): Found")

# (*) - character before can appear many times or not at all.
if re.search("ca*t","Look out for caaaat!."):
    print("(*): Found")

# (+) - Like star but character should must appear at least once
if re.search("ca+t","I have a ct. But also cut my finger."):
    print("(+): Found")
else:
    print("(+): Not found")

# (?) - character before is optional.
if re.search("colou?r","What color is it?"):
    print("(?): Found")