chuoi_nhap = input("nhập một mảng các số: ")
mang = [int(x) for x in chuoi_nhap.split()]

lon_nhat = max(mang)
nho_nhat = min(mang)

print(f"giá trị lớn nhất trong mảng:{lon_nhat}")
print(f"giá trị nhỏ nhất trong mảng:{nho_nhat}")