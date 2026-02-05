def tinh_tong(x):
    if x == 1:
        return 1
    else:
        return x + tinh_tong(x - 1)

n = int(input("Nhập n để tính tổng từ 1 đến n: "))
ket_qua = tinh_tong(n)
print(f"Tổng các số từ 1 đến {n} là: {ket_qua}")