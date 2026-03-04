danh_sach = [int(x) for x in input("Nhập các số nguyên khi nhập cách từng số: ").split()]

n = len(danh_sach)
so_lan_hoan_doi = 0

for i in range(n):
    for j in range(0, n - i - 1):
        if danh_sach[j] > danh_sach[j + 1]:
            danh_sach[j], danh_sach[j + 1] = danh_sach[j + 1], danh_sach[j]
            so_lan_hoan_doi += 1

print(f"Danh sách  sắp xếp:{danh_sach}")
print(f"Số lần hoán đổi thực hiện:{so_lan_hoan_doi}")