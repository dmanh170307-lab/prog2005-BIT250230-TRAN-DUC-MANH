ten_nhap_vao = "  nguyêN   văn  A  "
cac_tu = ten_nhap_vao.split()
danh_sach_tu_moi = []
for tu in cac_tu:
    tu_chuan = tu.capitalize()
    danh_sach_tu_moi.append(tu_chuan)
ten_chuan = " ".join(danh_sach_tu_moi)
print("Tên sau khi sửa:", ten_chuan)