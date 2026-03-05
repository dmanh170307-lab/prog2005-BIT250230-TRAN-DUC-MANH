from ftplib import print_line

try:
    a = int(input("Nhập số bị chia: "))
    b = int(input("Nhập số chia: "))

    kq = a / b
    print("Kết quả là:")
    print(kq)

except ValueError:
    print_line("Lỗi: phải nhập số nhé!")

except ZeroDivisionError:
    print("Lỗi: Không chia được cho 0.")