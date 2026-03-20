danh_sach_chuoi_b10 = []

print("Nhập 5 chuỗi ký tự bất kỳ:")
for i in range(5):
    chuoi = input(f"Chuỗi thứ {i + 1}: ")
    danh_sach_chuoi_b10.append(chuoi)
print("\nDanh sách ban đầu:", danh_sach_chuoi_b10)
n = len(danh_sach_chuoi_b10)
for i in range(n):
    for j in range(0, n - i - 1):
        if len(danh_sach_chuoi_b10[j]) < len(danh_sach_chuoi_b10[j + 1]):
            danh_sach_chuoi_b10[j], danh_sach_chuoi_b10[j + 1] = danh_sach_chuoi_b10[j + 1], danh_sach_chuoi_b10[j]
    print(f"Kết quả sau bước {i + 1}: {danh_sach_chuoi_b10}")