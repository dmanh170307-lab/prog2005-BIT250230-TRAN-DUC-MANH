for i in range(3):
    print("Nhập thông tin sinh viên thứ:", i + 1)
ten = input("Nhập tên sinh viên: ")
toan = float(input("Điểm Toán: "))
ly = float(input("Điểm Lý: "))
hoa = float(input("Điểm Hóa: "))
dtb = (toan + ly + hoa) / 3
print("Sinh viên:", ten)
print("Điểm trung bình:", dtb)