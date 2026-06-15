import random

password=""

for i in range(8):
    password+=str(random.randint(0,9))

print(password)
