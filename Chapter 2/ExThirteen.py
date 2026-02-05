mat_khau_dung = "manh2007@"
mat_khau_nhap = ""

while mat_khau_nhap != mat_khau_dung:
    mat_khau_nhap = input("mật khẩu: ")
    if mat_khau_nhap != mat_khau_dung:
        print("mật khẩu sai rồi, nhập lại!")

print("thành công!")