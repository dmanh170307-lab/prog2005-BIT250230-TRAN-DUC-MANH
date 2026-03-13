class Student:
    def __init__(self, ten, diem):
        self.ten = ten

        if 0 <= diem <= 10:
            self.diem = diem
        else:
            print(f"Lỗi:diểm {diem} sinh viên {ten} không hợp lệ!")
            self.diem = 0


sv_hop_le = Student("Tran duc manh", 9.0)
sv_loi = Student("Vu tr minh", 12)