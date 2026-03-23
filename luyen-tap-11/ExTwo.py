danh_sach = []
for i in range(5):
    danh_sach.append(input(f"Chuỗi thứ {i+1}: "))
danh_sach.sort(key=len, reverse=True)
print("\nDanh sách sau khi sắp xếp theo độ dài giảm dần:", danh_sach)
chuoi_tim_kiem = input("\nNhập chuỗi muốn tìm: ")
def tim_kiem_nhi_phan(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif len(arr[mid]) < len(target):
            right = mid - 1
        else:
            left = mid + 1
    return -1
vi_tri = tim_kiem_nhi_phan(danh_sach, chuoi_tim_kiem)
if vi_tri != -1:
    print(f"'{chuoi_tim_kiem}' nằm ở vị trí số[{vi_tri}]")
else:
    print(f"'{chuoi_tim_kiem}' trong danh sách.")