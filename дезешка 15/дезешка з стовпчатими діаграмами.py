import numpy as np
import matplotlib.pyplot as plt

naselenie2020 = np.array([ 83, 14000, 41, 67, 331])
naselenie2021 = np.array([84, 14100, 41, 67, 332])
labels = ['Німеччина', 'Китай', 'Україна', 'Британія', 'США']

plt.bar(labels, naselenie2020, label='населення країн 2020', color='lime', alpha=0.7)
plt.bar(labels, naselenie2021, label='населення країн 2021', color='red', alpha=0.7)

plt.xlabel('Країни')
plt.ylabel('Значення')
plt.legend()
plt.show()
