chuoi = input("Nhập một chuỗi: ")
ky_tu = input("Nhập ký tự cần đếm: ")

dem = 0
for c in chuoi:
    if c == ky_tu:
        dem = dem + 1

print(f"Ký tu '{ky_tu}' xuất hiện {dem} lần.")