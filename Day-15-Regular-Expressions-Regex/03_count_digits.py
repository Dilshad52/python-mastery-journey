import re

text = "Python123"

digits = re.findall(r"\d", text)

print(len(digits))
