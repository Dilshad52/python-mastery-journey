text = "python"

stack = []

for ch in text:
    stack.append(ch)

reverse = ""

while stack:
    reverse += stack.pop()

print(reverse)
