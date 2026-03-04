chuoi_nhap = input("nhập các số, cách nhau 1 lần cách: ")
danh_sach = [int(x) for x in chuoi_nhap.split()]

print("các số lẻ trong danh sách:")
for so in danh_sach:
    if so % 2 != 0:
        print(so, end=" ")