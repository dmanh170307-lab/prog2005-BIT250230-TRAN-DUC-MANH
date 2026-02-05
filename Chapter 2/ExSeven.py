a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

so1 = a
so2 = b

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(f"Ước chung cao nhất của {so1} và {so2} là: {a}")