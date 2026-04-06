diem1=float(input("Nhập điểm môn 1 : "))
diem2=float(input("Nhập điểm môn 2 : "))
diem3=float(input("Nhập điểm môn 3 : "))
dtb=(diem1+diem2+diem3)/3
print(f"Điểm trung bình 3 môn bằng : {dtb}")
if dtb>=8.0:
    print(" Xếp loại giỏi")
elif 6.5<=dtb<=7.9:
    print(" Xếp loại khá")
elif 5.0<=dtb<=6.4:
    print("Xếp loại Trung Bình")
else:
    print("Xếp loại yếu")
