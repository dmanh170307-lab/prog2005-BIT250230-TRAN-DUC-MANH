class Product:
    def __init__(self, price):
        self._price = 0
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print(f"giá nhập vào{price} phải > 0.")

    def __str__(self):
        return f"thông tin Giá = {self._price}"
sp1 = Product(150000)
print("sản phẩm 1:", sp1)

print("\nKhởi tạo sản phẩm 2:")
sp2 = Product(-500)
print("sản phẩm 2:", sp2)

print("\nCập nhật giá sản phẩm 2 thành 200000:")
sp2.set_price(200000)
print("Sản phẩm 2:", sp2)