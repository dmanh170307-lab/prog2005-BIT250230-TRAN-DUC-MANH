students = {
    "An": 8.5,
    "Bình": 7.0,
    "Chi": 9.0
}

def tinh_trung_binh(danh_sach):
    tong_diem = sum(danh_sach.values())
    so_luong = len(danh_sach)
    return tong_diem / so_luong

print(f"Điểm trung bình lớp: {tinh_trung_binh(students):.2f}")