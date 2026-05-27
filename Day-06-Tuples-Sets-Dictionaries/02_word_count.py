text = input("Enter sentence: ").split()

count = {}

for word in text:

    if word in count:
        count[word] += 1

    else:
        count[word] = 1

print(count)
