import re

email = input("Enter Email: ")

pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+$"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
