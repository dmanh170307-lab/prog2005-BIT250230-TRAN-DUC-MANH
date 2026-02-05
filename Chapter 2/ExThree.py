n = int(input("Nhập so n (số lượng số Fibonacci muốn in): "))

n1 = 0
n2 = 1
dem = 0

print("Dãy Fibonacci:")
if n <= 0:
    print("Vui lòng nhập số dương")
elif n == 1:
    print(n1)
else:
    while dem < n:
        print(n1, end=" ")
        so_tiep_theo = n1 + n2
        n1 = n2
        n2 = so_tiep_theo
        dem = dem + 1
print()