import re

text = "I love Python"

words = re.findall(r"\w+", text)

print(words)
