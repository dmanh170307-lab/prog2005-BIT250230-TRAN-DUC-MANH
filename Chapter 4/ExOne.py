def xuly_tuple(so_nguyen):
    if not so_nguyen:
        return 0, None, None

    tong = sum(so_nguyen)
    lon_nhat = max(so_nguyen)
    nho_nhat = min(so_nguyen)

    return tong, lon_nhat, nho_nhat

my_tuple = (9, 5, 8, -9, -3)
tong, max_val, min_val = xuly_tuple(my_tuple)
print(f"tuple: {my_tuple}")
print(f"tổng: {tong}")
print(f"giá trị lớn nhất: {max_val}")
print(f"giá trị nhỏ nhất: {min_val}")