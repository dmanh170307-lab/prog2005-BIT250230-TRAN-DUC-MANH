def tinh_tong(n):
    if n <=0:
        return 0
    if n==1:
        return 1
    return n+tinh_tong(n-1)
try:
    n=int(input("Nhập số nguyên dương "))
    if n<0:
        print("nhập lại số khác nguyên dương")
    else:
        kq=tinh_tong(n)
        print(f"tổng 1+2+...+n bằng {kq}")
except ValueError:
    print("Lỗi!")