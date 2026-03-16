chuoi = "TruongMINHoccho1234"
in_hoa = 0
in_thuong = 0
chu_so = 0
for ky_tu in chuoi:
    if ky_tu.isupper():
        in_hoa = in_hoa + 1
    elif ky_tu.islower():
        in_thuong = in_thuong + 1
    elif ky_tu.isdigit():
        chu_so = chu_so + 1
print("Chữ in hoa:", in_hoa)
print("Chữ in thường:", in_thuong)
print("Chữ số:", chu_so)