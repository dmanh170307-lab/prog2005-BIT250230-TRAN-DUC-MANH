input_str = input("nhập các số, cách nhau bằng dấu cách: ")
danh_sach = [int(x) for x in input_str.split()]

tim_thay = False

for so in danh_sach:
    if so > 10:
        print(f"số đầu tiên lớn hơn 10 là: {so}")
        tim_thay = True
        break

if not tim_thay:
    print("kh  số nào lớn hơn 10 trong danh sách.")