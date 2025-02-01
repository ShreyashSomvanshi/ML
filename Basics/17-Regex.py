import re

# Searching for a pattern
text = "The rain in Spain"
pattern = r"ain"

matches = re.findall(pattern, text)
print(matches)  # Output: ['ain', 'ain']
