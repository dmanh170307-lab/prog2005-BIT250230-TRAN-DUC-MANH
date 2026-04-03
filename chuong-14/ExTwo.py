danh_sach_ten = []
for i in range(5):
    ten = input(f"Nhập tên người {i+1}: ")
    danh_sach_ten.append(ten)
print(f"Danh sách mới là {danh_sach_ten}")

danh_sach_ten.pop(1)
print(f"Danh sách xóa tên thứ 2 là {danh_sach_ten}")