def generate(current, n):
    if len(current) == n:
        print(current)
        return

    generate(current + "0", n)
    generate(current + "1", n)

generate("", 3)
