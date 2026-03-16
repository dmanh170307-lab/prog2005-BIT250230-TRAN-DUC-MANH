class SinhVien:
    tong_so_sinh_vien = 0

    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
        SinhVien.tong_so_sinh_vien = SinhVien.tong_so_sinh_vien + 1
    @classmethod
    def dem_si_so(cls):
        print(f"tổng số sinh viên hiện tại: {cls.tong_so_sinh_vien}")
print("lúc đầu")
SinhVien.dem_si_so()
sv1 = SinhVien("An", 8.5)
sv2 = SinhVien("Bình", 9.0)
sv3 = SinhVien("Cường", 7.5)

print("\nsau khi nhận 3 bạn")
SinhVien.dem_si_so()