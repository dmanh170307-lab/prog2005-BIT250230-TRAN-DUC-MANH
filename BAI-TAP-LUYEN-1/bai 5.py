import random

M = int(input("nhập số hàng M: "))
N = int(input("nhập số cột N: "))

ma_tran = []
for i in range(M):
    hang = []
    for j in range(N):
        hang.append(random.randint(1, 100))
    ma_tran.append(hang)

print("\nma trậntạo:")
for hang in ma_tran:
    print(hang)

hang_xem = int(input(f"\nnhập số thứ tự hàng muốn (từ 0 đến {M-1}): "))
print(f"dữ liệu hàng {hang_xem}: {ma_tran[hang_xem]}")

cot_xem = int(input(f"nhập số thứ tự cột muốn (từ 0 đến {N-1}): "))
cot_data = [ma_tran[i][cot_xem] for i in range(M)]
print(f"dữ liệu cột {cot_xem}: {cot_data}")

gia_tri_max = max(max(hang) for hang in ma_tran)
print("\ngiá trị lớn nhất trog ma trận:", gia_tri_max)