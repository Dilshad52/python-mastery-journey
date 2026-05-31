with open("source.txt", "r") as source:

    data = source.read()

with open("target.txt", "w") as target:

    target.write(data)
