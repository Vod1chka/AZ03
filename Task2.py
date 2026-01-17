import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(5)
y = np.random.rand(5)

print("x:", x)
print("y:", y)

plt.figure()
plt.scatter(x, y)
plt.title("Диаграмма рассеяния случайных данных")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()