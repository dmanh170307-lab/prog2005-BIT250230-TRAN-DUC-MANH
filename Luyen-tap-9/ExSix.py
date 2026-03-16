class Product:
    def __init__(self, price):
        self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, gia_tien_moi):
        if gia_tien_moi > 0:
            self._price = gia_tien_moi
        else:
            print("Lỗi: Giá tiền không nhỏ hơn 0!")
    def __str__(self):
        return f"Sản phẩm này có giá: {self.price}"
sp = Product(500)
print(sp)