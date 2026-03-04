danh_sach_mau=["pink","blue","black","red","yellow"]
print(f"danh sách màu ban đầu: {danh_sach_mau}")
try:
    danh_sach_mau.remove("Green")
    print("xóa màu green xong")
except:
    print("Lỗi: Không có màu Green trong danh sách để xóa")
print(f"danh sách sau khi xử lí {danh_sach_mau}")