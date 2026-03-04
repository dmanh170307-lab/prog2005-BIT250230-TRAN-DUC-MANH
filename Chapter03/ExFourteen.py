def count_vowels(s):
    dem = 0
    nguyen_am = "aeiou"

    s_thuong = s.lower()

    for ky_tu in s_thuong:
        if ky_tu in nguyen_am:
            dem += 1

    return dem


chuoi_kiem_tra = input("nhập chuỗi cần đếm nguyên âm: ")
ket_qua = count_vowels(chuoi_kiem_tra)
print(f"số lượng nguyên am trong chuỗi là: {ket_qua}")