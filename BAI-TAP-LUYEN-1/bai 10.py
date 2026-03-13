TEN_FILE = "sanpham.txt"

def them_san_pham():
    ma_sp = input("nhập mã sp: ")
    ten_sp = input("nhập tên sp: ")

    while True:
        try:
            gia_sp = float(input("nhập giá: "))
            break
        except ValueError:
            print("Lỗi: nhap lại đi")

    with open(TEN_FILE, "a", encoding="utf-8") as file:
        file.write(f"{ma_sp};{ten_sp};{gia_sp}\n")

    print("đã thêm sản phẩm thành công!")


def hien_thi_danh_sach():
    try:
        with open(TEN_FILE, "r", encoding="utf-8") as file:
            du_lieu = file.read()
            if len(du_lieu) == 0:
                print("tệp hiện kocó dữ liệu.")
            else:
                print(du_lieu.strip())
    except FileNotFoundError:
        print("tệp k tồn tại")


def sap_xep_giam_dan():
    try:
        with open(TEN_FILE, "r", encoding="utf-8") as file:
            danh_sach_sp = []

            for dong in file:
                thong_tin = dong.strip().split(";")

                if len(thong_tin) == 3:
                    ma = thong_tin[0]
                    ten = thong_tin[1]
                    gia = float(thong_tin[2])

                    danh_sach_sp.append([ma, ten, gia])

            def lay_gia(san_pham):
                return san_pham[2]

            danh_sach_sp.sort(key=lay_gia, reverse=True)
            for sp in danh_sach_sp:
                print(f"{sp[0]};{sp[1]};{sp[2]}")

    except FileNotFoundError:
        print("tệp khong tồn tại")


while True:
    print("1. nhập thêm sản phẩm")
    print("2. danh sách sản phẩm")
    print("3. sắp xếp giá giảm dần")
    print("0. thoát chương trình")

    lua_chon = input("nhập lựa chọn (0-3): ")

    if lua_chon == '1':
        them_san_pham()
    elif lua_chon == '2':
        hien_thi_danh_sach()
    elif lua_chon == '3':
        sap_xep_giam_dan()
    elif lua_chon == '0':
        print("dã thoát !")
        break
    else:
        print("lựa chọn không hợp lệ!")
