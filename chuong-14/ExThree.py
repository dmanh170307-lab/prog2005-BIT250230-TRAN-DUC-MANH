import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

chuoi_nhap = input("Nhập mảng các số tự nhiên : ")
mang = [int(x) for x in chuoi_nhap.split()]

so_le = [x for x in mang if x % 2 != 0]
print(f"Dòng 1: Các số lẻ là {so_le} và tổng số lượng số lẻ là {len(so_le)}")

so_nguyen_to = [x for x in mang if is_prime(x)]
print(f"Dòng 2: Các số nguyên tố là {so_nguyen_to}")