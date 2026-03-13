print("từ 1 đến 100 (bỏ số chia hết cho 3):")
for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()