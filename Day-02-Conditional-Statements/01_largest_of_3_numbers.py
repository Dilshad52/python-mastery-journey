a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a > b and a > c:
    print("Largest =", a)

elif b > a and b > c:
    print("Largest =", b)

else:
    print("Largest =", c)
