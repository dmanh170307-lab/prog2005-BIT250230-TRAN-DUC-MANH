class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price
sach1 = Book("Book 1", 30000)
sach2 = Book("Book 2", 50000)
sach3 = Book("Book 3", 100000)
danh_sach = [sach1, sach2, sach3]
tong_tien = 0
f = open("bai5.txt", "w")

for s in danh_sach:
    ten = s.get_name()
    gia = s.get_price()
    f.write(ten + ";" + str(gia) + "\n")
    tong_tien = tong_tien + gia
f.write("Tong;" + str(tong_tien))
f.close()
print("Đã tạo và ghi xong dữ liệu vào file bai5.txt")