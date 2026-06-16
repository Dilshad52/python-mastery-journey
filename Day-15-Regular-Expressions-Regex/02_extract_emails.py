import re

text = "abc@gmail.com xyz@yahoo.com"

emails = re.findall(
    r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+",
    text
)

print(emails)
