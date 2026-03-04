chuoi = input("nhập một chuỗi  kiểm tra: ")

chuoi_dao_nguoc = chuoi[::-1]

if chuoi == chuoi_dao_nguoc:
    print("dây là chuỗi đối xứng (Palindrome).")
else:
    print("đây không phải là chuỗi đối xứng.")