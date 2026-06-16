import re

text = "Order 123 Price 500"

print(re.findall(r"\d+", text))
