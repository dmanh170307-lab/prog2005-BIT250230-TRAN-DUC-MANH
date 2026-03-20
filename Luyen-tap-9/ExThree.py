def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * tinh_giai_thua(n - 1)
so = int(input("Nhập một số nguyên dương tính giai thừa: "))

if so < 0:
    print("Lỗi không có giai thừa cho số âm!")
else:
    ket_qua = tinh_giai_thua(so)
    print(f"Giai thừa của {so}! là: {ket_qua}")