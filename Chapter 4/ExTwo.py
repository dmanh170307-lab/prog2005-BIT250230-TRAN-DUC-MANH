def tinh_diem_trung_binh(danh_sach):

    if not danh_sach:
        return 0

    tong_diem = sum(danh_sach.values())
    so_luong_sv = len(danh_sach)
    diem_tb = tong_diem / so_luong_sv
    return diem_tb

sinh_vien_dict = {"Manh":9,"Quan":8,"Trang":6}
diem_trung_binh = tinh_diem_trung_binh(sinh_vien_dict)
print(f"danh sách điểm: {sinh_vien_dict}")
print(f"diểm trung bình các sinh viên: {diem_trung_binh}")