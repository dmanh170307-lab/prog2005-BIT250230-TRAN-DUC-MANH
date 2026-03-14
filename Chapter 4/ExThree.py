def kiem_tra_key(dictionary, key_can_tim):

    if key_can_tim in dictionary:
        print(f"Key '{key_can_tim}'  tồn tại trong dictionary.")
    else:
        print(f"Key '{key_can_tim}' ko tồn tại trong dictionary.")

my_dict = {"ten": "Minh", "tuoi": 18, "nganh": "CNTT"}

print(f"Dictionary hiện tại: {my_dict}")
kiem_tra_key(my_dict, "tuoi")
kiem_tra_key(my_dict, "dia_chi")