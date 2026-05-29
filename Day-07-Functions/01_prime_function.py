def prime(n):

    count = 0

    for i in range(1, n + 1):

        if n % i == 0:
            count += 1

    if count == 2:
        return "Prime"

    return "Not Prime"


print(prime(7))
