class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price
my_book = Book("Lập trình Python", 150000)
print(f"Giá của đối tượng sách là: {my_book.get_price()}")