class Counter:

    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.max_num:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


counter = Counter(10)

for num in counter:
    print(num)
