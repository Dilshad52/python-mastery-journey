text = input("Enter text: ").lower()

count = 0

for ch in text:

    if ch in "aeiou":
        count = count + 1

print("Vowels =", count)
