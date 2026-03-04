chuoi = input("nhập chuỗi cần đảo ngược: ")

cach_1 = chuoi[::-1]
print(f"Cách 1dùng slicing: {cach_1}")

cach_2 = "k dung"
for ky_tu in chuoi:

    cach_2 = ky_tu + cach_2

print(f"cách 2 kh dùng slicing): {cach_2}")