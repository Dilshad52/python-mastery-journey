import re

text = """
Name: Dilshad
Email: dilshad@gmail.com
Phone: 9876543210
Message: Hello@#Python123!
"""

emails = re.findall(
    r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+",
    text
)

numbers = re.findall(r"\d+", text)

clean_text = re.sub(
    r"[^a-zA-Z0-9\s]",
    "",
    text
)

print("Emails:", emails)
print("Numbers:", numbers)

print("\nCleaned Text:")
print(clean_text)
