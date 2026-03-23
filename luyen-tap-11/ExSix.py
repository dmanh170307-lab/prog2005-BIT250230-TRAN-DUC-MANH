so_nguoi = int(input("nhập thông tin bao nhiêu người:"))
danh_sach_nguoi = {}

for i in range(so_nguoi):
    print(f"\n Người thứ {i + 1}")
    ten = input("Nhập tên: ")
    tuoi = int(input(f"Nhập tuổi "))

    danh_sach_nguoi[ten] = tuoi
print("\nDữ liệu Dictionary vừa tạo:",danh_sach_nguoi)
if so_nguoi > 0:
    tong_tuoi = sum(danh_sach_nguoi.values())
    tuoi_trung_binh = tong_tuoi / so_nguoi
    print(f"Tuổi trung bình của {so_nguoi} người là: {tuoi_trung_binh}")
else:
    print("Danh sách trống.")