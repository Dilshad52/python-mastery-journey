a=int(input())
b=int(input())

op=input("Enter +,-,*,/: ")

if op=="+":
    print(a+b)

elif op=="-":
    print(a-b)

elif op=="*":
    print(a*b)

elif op=="/":
    print(a/b)

else:
    print("Invalid Operator")
