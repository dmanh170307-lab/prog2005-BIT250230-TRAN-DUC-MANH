ma_tran_A = [[1, 2, 3],
             [4, 5, 6]]

ma_tran_B = [[7, 8, 9],
             [10, 11, 12]]

ket_qua = [[0, 0, 0],
           [0, 0, 0]]

so_hang = len(ma_tran_A)
so_cot = len(ma_tran_A[0])

for i in range(so_hang):
    for j in range(so_cot):
        ket_qua[i][j] = ma_tran_A[i][j] + ma_tran_B[i][j]

print("ma trận kết quả sau khi cộng:")
for hang in ket_qua:
    print(hang)