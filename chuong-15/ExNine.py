def save_to_file():
    content = input("Nhập chuỗi ký tự bất kỳ: ")
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("Đã lưu file")

save_to_file()