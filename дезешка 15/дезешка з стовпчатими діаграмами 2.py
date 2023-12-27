import numpy as np
import matplotlib.pyplot as plt

categories = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд']
var = [-1723, 8357, 3456, -5564, 3758, 46589, 3465]


plt.bar(categories, var, color='blue')


plt.title('прибуток магазину за кожен день тижня грн')
plt.xlabel('День тижня')
plt.ylabel('грн')


plt.show()
