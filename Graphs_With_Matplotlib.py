import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.random.rand(10) * 100
y4 = np.random.randn(1000)

plt.subplot(2, 2, 1)
plt.plot(x, y1, label= "Sin(x)", color = "b")
plt.plot(x, y2, label= "Cos(x)", color = "r")
plt.title("Çizgi Grafiği")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.subplot(2, 2, 2)
plt.bar(range(10), y3, color= "g")
plt.title("Çubuk Grafiği")
plt.xlabel("Kategori")
plt.ylabel("Değer")

plt.subplot(2, 2, 3)
plt.scatter(x, y1, label="Sin(x)", color="b", alpha= 0.5)
plt.scatter(x, y1, label="Cos(x)", color="r", alpha= 0.5)
plt.title("Dağılım Grafiği")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.subplot(2, 2, 4)
plt.hist(y4, bins=30, color="m", edgecolor="black")
plt.title("Histogram")
plt.xlabel("Değer")
plt.ylabel("Frekans")

plt.tight_layout()

plt.show()
