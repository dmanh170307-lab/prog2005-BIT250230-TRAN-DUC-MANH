chuoi_nhap = input("Nhập chuỗi các số cách nhau bằng dấu chấm phẩy (VD: 5; 7; -2): ")

danh_sach_so = [int(x.strip()) for x in chuoi_nhap.split(";")]

print("\n- Từng số trên một dòng:")
for so in danh_sach_so:
    print(so)

so_chan = [x for x in danh_sach_so if x % 2 == 0]
print(f"- có {len(so_chan)} số chẵn.")

so_am = [x for x in danh_sach_so if x < 0]
print(f"- có {len(so_am)} số âm.")

def kiem_tra_nguyen_to(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

so_nguyen_to = [x for x in danh_sach_so if kiem_tra_nguyen_to(x)]
print(f"- có {len(so_nguyen_to)} số nguyên tố.")

trung_binh = sum(danh_sach_so) / len(danh_sach_so)
print(f"- giá trị trung bình: {trung_binh}")