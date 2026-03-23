danh_sach_chuoi = []
for i in range(5):
    chuoi = input(f"Nhập chuỗi {i + 1}:")
    danh_sach_chuoi.append(chuoi)
print("\nSắp xếp Insertion Sort:")

for i in range(1, len(danh_sach_chuoi)):
    key = danh_sach_chuoi[i]
    j = i - 1
    while j >= 0 and len(key) > len(danh_sach_chuoi[j]):
        danh_sach_chuoi[j + 1] = danh_sach_chuoi[j]
        j -= 1
    danh_sach_chuoi[j + 1] = key
    print(f"Bước {i}: {danh_sach_chuoi}")
print("\nChuỗi sắp xếp xong:", danh_sach_chuoi)