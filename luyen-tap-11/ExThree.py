n = int(input("Nhập bao nhiêu số nguyên"))
danh_sach_so = []

for i in range(n):
    so = int(input(f"Nhập số thứ {i+1}: "))
    danh_sach_so.append(so)

tong_chan = 0
print("\nCác số chẵn danh sách: ", end="")
for so in danh_sach_so:
    if so % 2 == 0:
        print(so, end=" ")
        tong_chan += so
print(f"\nTổng của các số chẵn: {tong_chan}")