thong_tin= {'tin hoc':9,'toan':7,'van':6,'anh':5 }
print("Dictionary hiện tại:", thong_tin)

key_can_tim = input("\nNhập 'key' bạn muốn kiểm tra xem có tồn tại không: ")

if key_can_tim in thong_tin:
    print(f"Key'{key_can_tim}'tồn tại trong dictionary Giá trị: {thong_tin[key_can_tim]}.")
else:
    print(f" không tồn tại trong dictionary.")