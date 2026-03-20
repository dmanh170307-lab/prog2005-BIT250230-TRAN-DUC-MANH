class SinhVien:
    truong_hoc = "Đại học CMC"

    def __init__(self, ten, diem):
        self._ten = ten
        self.set_diem(diem)

    def get_ten(self):
        return self._ten

    def set_ten(self, ten_moi):
        self._ten = ten_moi

    def get_diem(self):
        return self._diem

    def set_diem(self, diem_moi):
        if diem_moi < 0 or diem_moi > 10:
            raise ValueError("Lỗi 1: Điểm phải từ 0 đến 10")
        self._diem = diem_moi

    def thong_bao_hoc_tap(self):
        return f"Sinh viên {self._ten} đang học bài."

    @classmethod
    def thong_tin_truong(cls):
        return f"Trường đang học: {cls.truong_hoc}"

    @staticmethod
    def quy_doi_diem_he_4(diem_he_10):
        return diem_he_10 * 0.4

    def __str__(self):
        return f"[SinhVien] Tên: {self._ten}, Điểm: {self._diem}"

    def __eq__(self, sinh_vien_khac):
        if isinstance(sinh_vien_khac, SinhVien):
            return self._diem == sinh_vien_khac.get_diem()
        return False

class LopTruong(SinhVien):
    def __init__(self, ten, diem, nhiem_vu):
        super().__init__(ten, diem)

        if nhiem_vu == "":
            raise ValueError("Lỗi 2: Lớp trưởng có nhiệm vụ cụ thể!")
        self.nhiem_vu = nhiem_vu

    def __str__(self):
        return f"[LopTruong] Tên: {self._ten}, Điểm: {self._diem}, Nhiệm vụ: {self.nhiem_vu}"

sv1 = SinhVien("An", 8)
sv2 = SinhVien("Bình", 8)
lt = LopTruong("Châu", 9, "Điểm danh")

print(sv1)  # Gọi hàm __str__
print(lt)

print("Instance method:", sv1.thong_bao_hoc_tap())
print("Class method:", SinhVien.thong_tin_truong())
print("Static method (Đổi điểm 8 sang hệ 4):", SinhVien.quy_doi_diem_he_4(8))
print(f"Nạp chồng toán tử == (An và Bình bằng điểm nhau?): {sv1 == sv2}")

try:
    sv_loi = SinhVien("Dũng", 15)
except ValueError as e:
    print(e)

try:
    lt_loi = LopTruong("Giang", 7, "")
except ValueError as e:
    print(e)