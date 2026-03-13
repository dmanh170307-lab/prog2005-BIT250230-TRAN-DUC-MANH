so = int(input("nhap số 1-->9:"))

if 1 <= so <= 9:
    print(f"bảng cửu chương {so}")
    for i in range(1, 10):
        print(f"{so}x{i} = {so*i}")
else:
    print("chỉ nhận số 1-->9.")