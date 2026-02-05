n = int(input("Nhập 1 số: "))
temp = n
tong = 0

while n > 0:
    chu_so = n % 10
    tong = tong + chu_so
    n = n // 10

print(f"tổng các số của {temp} là: {tong}")