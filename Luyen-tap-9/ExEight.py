danh_sach_chuoi = []

print("Nhập 5 chuỗi bất kỳ:")
for i in range(5):
    chuoi = input(f"Chuỗi thứ {i + 1}: ")
    danh_sach_chuoi.append(chuoi)
print("\nDanh sách ban đầu:", danh_sach_chuoi)
n = len(danh_sach_chuoi)
for i in range(n):
    for j in range(0, n - i - 1):
        if len(danh_sach_chuoi[j]) < len(danh_sach_chuoi[j + 1]):
            danh_sach_chuoi[j], danh_sach_chuoi[j + 1] = danh_sach_chuoi[j + 1], danh_sach_chuoi[j]
    print(f"Kết quả sau bước {i + 1}: {danh_sach_chuoi}")