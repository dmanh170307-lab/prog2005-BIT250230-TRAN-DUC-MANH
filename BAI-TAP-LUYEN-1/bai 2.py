import math
so1 = float(input("nhập số thứ nhất: "))
so2 = float(input("nhập số thứ hai: "))
kq=so1**so2
print("lũy thừa(số 1 ^ số 2):", kq)
if so1 >= 0:
    print("căn bậc 2 số 1:", math.sqrt(so1))
else:
    print("lỗi")

if so2 != 0:
    print("chia lấy phần nguyên:", so1 // so2)
    print("chia lấy phần dư:", so1 % so2)
else:
    print("Lỗi:không chia cho 0.")

print("làm tròn số 1:", round(so1))