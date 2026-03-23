import csv

ten = input("Nhập tên Nhân viên: ")
tuoi = input("Nhập tuổi: ")
ma_id = input("Nhập ID nhân viên: ")

with open("thongtin.txt", "w", encoding="utf-8") as file_txt:
    file_txt.write(f"Nhân viên: {ten}, Tuổi: {tuoi}, ID: {ma_id}\n")
print("\n-> Đã lưu thành công vào file text: 'thongtin.txt'")

with open("thongtin.csv", "w", newline='', encoding="utf-8") as file_csv:
    ghi_csv = csv.writer(file_csv)
    ghi_csv.writerow(["Tên", "Tuổi", "ID"])
    ghi_csv.writerow([ten, tuoi, ma_id])
print("-> Đã lưu thành công vào file csv: 'thongtin.csv'")