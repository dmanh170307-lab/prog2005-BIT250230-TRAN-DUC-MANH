n = int(input("Nhập một số dương: "))

if n < 2:
    print(f"{n} không phải là số nguyên tố")
else:
    la_nguyen_to = True
    for i in range(2, n):
        if n % i == 0:
            la_nguyen_to = False
            break

    if la_nguyen_to == True:
        print(f"{n} là số nguyen to")
    else:
        print(f"{n} kh là số nguyên tố")