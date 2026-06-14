class Bank:

    def __init__(self):
        self.__balance = 10000

    def show(self):
        print(self.__balance)


b = Bank()

b.show()
