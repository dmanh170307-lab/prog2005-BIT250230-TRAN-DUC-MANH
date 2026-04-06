def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
n=int(input("nhập số nguyên tính giai thừa:"))
if n<0:
    print("số âm loại")
else:
    print(f"Giai thừa là : {factorial(n)}")