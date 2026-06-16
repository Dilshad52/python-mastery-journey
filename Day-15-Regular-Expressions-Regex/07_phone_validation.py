import re

phone = input("Enter Phone Number: ")

pattern = r"^\d{10}$"

if re.match(pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")
