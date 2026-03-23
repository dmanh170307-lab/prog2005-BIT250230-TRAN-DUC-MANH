def nhap_ma_tran(so_hang, so_cot, ten_ma_tran):
    print(f"\nNhập ma trận {ten_ma_tran}:")
    ma_tran = []
    for i in range(so_hang):
        hang = []
        for j in range(so_cot):
            gia_tri = input(f"Nhập số ở vị trí [{i}][{j}]: ")
            if gia_tri.strip() == "":
                raise ValueError(f"để trống [{i}][{j}]!")

            hang.append(int(gia_tri))
        ma_tran.append(hang)
    return ma_tran


try:
    hang = int(input("Nhập số lượng hàng:"))
    cot = int(input("Nhập số lượng cột:"))

    ma_tran_A = nhap_ma_tran(hang, cot, "A")
    ma_tran_B = nhap_ma_tran(hang, cot, "B")

    ma_tran_ket_qua = []
    for i in range(hang):
        hang_moi = []
        for j in range(cot):
            hang_moi.append(ma_tran_A[i][j] + ma_tran_B[i][j])
        ma_tran_ket_qua.append(hang_moi)
    print("\nKết quả Ma trận A+B:")
    for h in ma_tran_ket_qua:
        print(h)
except ValueError as e:
    print(f"\nKết thúc {e}")