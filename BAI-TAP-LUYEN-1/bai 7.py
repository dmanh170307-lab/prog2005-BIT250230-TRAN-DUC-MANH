
class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

sv1 = Student("Tran duc manh", 8.5)
sv2 = Student("Vu truong minh", 7.0)

print("tên SV1:", sv1.ten, "|diểm SV1:", sv1.diem)
print("tên SV2:", sv2.ten, "|diểm SV2:", sv2.diem)