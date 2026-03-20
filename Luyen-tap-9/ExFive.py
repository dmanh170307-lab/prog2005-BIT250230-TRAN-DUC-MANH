import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.plot(x, x**2, color='blue')
ax1.set_title("Đồ thị y = x^2")
ax1.set_xlabel("Trục x")
ax1.set_ylabel("Trục y")

ax2.plot(x, np.sqrt(x), color='red')
ax2.set_title("Đồ thị y = căn bậc 2 của x")
ax2.set_xlabel("Trục x")
ax2.set_ylabel("Trục y")

plt.tight_layout()
plt.show()
