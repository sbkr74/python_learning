import re

# Finding all Matches in a String.
words = "fear, gear, tear, tire"
all_matches = re.findall(".ear",words)
print(all_matches)