class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
    def __str__(self):
        return f"tên hoa: {self.ten}-Màu sắc: {self.mau}"
hoa_hong = Hoa("Hoa Hồng","đỏ")
print(hoa_hong)