def decimal_to_binary(n):
    stack = []

    while n > 0:
        stack.append(n % 2)
        n //= 2

    while stack:
        print(stack.pop(), end="")


decimal_to_binary(10)
