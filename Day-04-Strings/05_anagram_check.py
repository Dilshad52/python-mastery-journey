a = input("Enter first word: ")
b = input("Enter second word: ")

if sorted(a) == sorted(b):
    print("Anagram")

else:
    print("Not Anagram")
