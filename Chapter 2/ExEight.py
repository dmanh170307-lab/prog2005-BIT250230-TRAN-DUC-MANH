n = int(input("Nhập số cần đảo ngược: "))
so_goc = n
so_dao = 0

while n > 0:
    chu_so = n % 10
    so_dao = so_dao * 10 + chu_so
    n = n // 10

print(f"Số đảo ngược của {so_goc} là: {so_dao}")