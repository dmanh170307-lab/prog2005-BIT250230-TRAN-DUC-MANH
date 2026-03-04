chuoi_nhap = input("nhập các số, cách nhau 1 lần cách: ")
danh_sach = [int(x) for x in chuoi_nhap.split()]

tong_chan = 0

print("các số chẵn trong danh sách là:")
for so in danh_sach:
    if so % 2 == 0:
        print(so, end=" ")
        tong_chan += so

print(f"\ntổng của các số chẵn:{tong_chan}")