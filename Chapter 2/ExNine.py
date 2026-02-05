n = int(input("Nhập số nguyên dương 5 chữ số: "))

max_so = 0

while n > 0:
    chu_so = n % 10
    if chu_so > max_so:
        max_so = chu_so
    n = n // 10

print(f"Chữ số lớn nhất là: {max_so}")