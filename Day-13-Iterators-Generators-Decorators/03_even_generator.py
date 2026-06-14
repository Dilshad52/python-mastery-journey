# even_generator.py

def even_numbers(n):
    """
    Generator that yields even numbers from 2 to n
    """

    for i in range(2, n + 1, 2):
        yield i


# Example Usage
for num in even_numbers(20):
    print(num)
