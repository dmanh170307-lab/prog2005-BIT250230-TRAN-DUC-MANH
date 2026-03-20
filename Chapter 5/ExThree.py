import matplotlib.pyplot as plt

san_pham = ['A', 'B', 'C', 'D', 'E']
phan_tram = [30, 25, 15, 20, 10]

plt.pie(phan_tram, labels=san_pham, autopct='%1.1f%%', startangle=90)
plt.title('Phần trăm doanh số của 5 sản phẩm')

plt.show()