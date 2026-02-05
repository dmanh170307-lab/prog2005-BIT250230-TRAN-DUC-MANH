def tinh_giai_thua(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * tinh_giai_thua(x - 1)

n = int(input("Nhập số cần tính giai thừa: "))
ket_qua = tinh_giai_thua(n)
print(f"Giai thừa của {n} là: {ket_qua}")