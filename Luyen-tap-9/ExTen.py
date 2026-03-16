class SinhVien:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
    def __eq__(self, sinh_vien_khac):
        if self.diem == sinh_vien_khac.diem:
            return True
        else:
            return False
sv1 = SinhVien("Minh", 8.5)
sv2 = SinhVien("Dune", 8.5)
sv3 = SinhVien("dũng", 7.0)
if sv1 == sv2:
    print("minh dung bằng điểm nhau")
else:
    print("minh dune ko bằng điểm nhau")

if sv1 == sv3:
    print("minh dũng bằng nhau")
else:
    print("minh dũng k bằng điểm nhau")