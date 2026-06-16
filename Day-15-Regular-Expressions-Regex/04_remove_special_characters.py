import re

text = "Hello@#Python123!"

clean = re.sub(r"[^a-zA-Z0-9 ]", "", text)

print(clean)
