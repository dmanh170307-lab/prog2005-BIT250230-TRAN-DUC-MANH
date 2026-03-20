import os
def co_duoi(duong_dan):
    return os.path.basename(duong_dan)
def khong_duoi(duong_dan):
    ten_file = os.path.basename(duong_dan)
    ten, duoi = os.path.splitext(ten_file)
    return ten
duong_dan_nhac = r"d:\music\muabui.mp3"
print("Đường dẫn:", duong_dan_nhac)
print("hàm 1:", co_duoi(duong_dan_nhac))
print("hàm 2:", khong_duoi(duong_dan_nhac))
