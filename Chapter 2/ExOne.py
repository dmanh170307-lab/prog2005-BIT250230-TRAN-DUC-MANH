n = int(input("nhap 1 số từ 1 -->9: "))
if 1 <= n <= 9:
    print(f"bảng cửu chuong số {n} :")
    for i in range(1, 10):
        print(f"{n} x {i} = {n * i}")
else:
    print("nhập số từ 1-->9")