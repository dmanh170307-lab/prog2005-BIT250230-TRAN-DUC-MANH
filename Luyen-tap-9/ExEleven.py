while True:
    choice = input("chon bai")
    if choice == "0":
        break
    elif choice == "1":
        import os
        path = input("nhap huong dan")
        print(os.path.basename(path))
        print(os.path.splitext(os.path.basename(path))[0])
    elif choice == "2":
        s = input("nhap chuoi")
        c = input("nhap ky tu")
        print(s.count(c))
    elif choice == "3":
        n = int(input("nhap so"))
        f = 1
        for i in range(1, n+1):
            f *= i
        print(f)
    elif choice == "4":
        s = input("nhap chuoi")
        print(len(s) if s else "loi")
    elif choice == "5":
        import matplotlib.pyplot as plt
        import numpy as np
        fig, (ax1, ax2) = plt.subplots(1, 2)
        x = np.linspace(0, 10, 100)
        ax1.plot(x, x**2)
        ax1.set_title("y=x^2")
        ax2.plot(x, np.sqrt(x))
        ax2.set_title("y=sqrt(x)")
        plt.show()
    elif choice == "6":
        s = input("nhap chuoi")
        print(s[::-1])
    elif choice == "7":
        while input("mk") != "anh minh dep trai nhat the gioi":
            print("sai")
        print("ok")
    elif choice == "8":
        arr = [input(f"Chuỗi {i+1}: ") for i in range(5)]
        n = len(arr)
        for i in range(n-1):
            for j in range(n-1-i):
                if len(arr[j]) < len(arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"Bước {i+1}: {arr}")
    elif choice == "9":
        print("tu test")
    elif choice == "10":
        arr = [input(f"Chuỗi {i+1}: ") for i in range(5)]
        n = len(arr)
        for i in range(n-1):
            for j in range(n-1-i):
                if len(arr[j]) < len(arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"b {i+1}: {arr}")
    else:
        print("chon lai")