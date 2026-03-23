import math

def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

danh_sach = [5, 2, 9, 8, 2, 7, 3]
print("Danh sách ban đầu:", danh_sach)

danh_sach.append(15)
print("Danh sách thêm số:", danh_sach)

k = int(input("\nNhập số nguyên để đếm số lần xuất hiện: "))
so_lan = danh_sach.count(k)
print(f"-> Số {k} xuất hiện {so_lan} lần trong danh sách.")

tong_nguyen_to = 0
for x in danh_sach:
    if la_so_nguyen_to(x):
        tong_nguyen_to += x
print(f"\n- Tổng các số nguyên tố trong danh sách là: {tong_nguyen_to}")

danh_sach.sort()
print(f"- Danh sách sau khi sắp xếp tăng dần: {danh_sach}")

danh_sach.clear()
print(f"- Danh sách sau khi chạy lệnh xóa (clear): {danh_sach}")