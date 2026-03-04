danh_sach_so = []

so_luong = int(input(" muốn nhập bao nhiêu số? "))

for i in range(so_luong):
    so_nhap_vao = float(input(f"Nhập số thứ {i + 1}: "))
    danh_sach_so.append(so_nhap_vao)

print(f"danh sách số  vừa nhập là:{danh_sach_so}")

for i in range(1, len(danh_sach_so)):
    key = danh_sach_so[i]

    j = i - 1

    while j >= 0 and danh_sach_so[j] < key:
        danh_sach_so[j + 1] = danh_sach_so[j]
        j = j - 1

    danh_sach_so[j + 1] = key

print("Danh sách sau khi sắp xếp:{danh_sach_so}"))