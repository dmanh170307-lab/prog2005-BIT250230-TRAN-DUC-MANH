n = int(input("Nhập một số n để kiểm tra xem là nguyên tố kh: "))

if n < 2:
    print(f"{n} không phai số nguyên tố")
else:
    kiem_tra = True
    for i in range(2, n):
        if n % i == 0:
            kiem_tra = False
            break

    if kiem_tra == True:
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không là số nguyên tố")