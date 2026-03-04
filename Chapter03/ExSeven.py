input_str = input("nhập các số, cách nhau dấu cách: ")
danh_sach = [int(x) for x in input_str.split()]

target = int(input("nhập số cần tìm chỉ số: "))

vi_tri = -1

for i in range(len(danh_sach)):
    if danh_sach[i] == target:
        vi_tri = i
        break

if vi_tri != -1:
    print(f"số {target} nằm ở chỉ số (vị trí): {vi_tri}")
else:
    print(f"không tìm thấy số {target} trong danh sách.")