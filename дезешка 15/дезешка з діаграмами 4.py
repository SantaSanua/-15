import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)
y1 = x*x
y2 = x*x*x

plt.plot(x, y1, label='y1 = x^2')
plt.plot(x, y2, label='y2 = x^3')
plt.fill_between(x, y1, y2, color='gray', alpha=0.3, label='Інтеграл')

plt.legend()
plt.title('Інтеграл між кривими y1 та y2')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
