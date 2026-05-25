text = input("Enter text: ")
ch = input("Enter character: ")

count = 0

for i in text:

    if i == ch:
        count = count + 1

print("Frequency =", count)
