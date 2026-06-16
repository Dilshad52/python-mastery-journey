import re

password = input("Enter Password: ")

pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"

if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")
