import matplotlib.pyplot as plt
import numpy as np

xpoints_Pillow = np.array([0, 2, 5, 8, 10])
ypoints = np.array([0, 2, 4, 6, 8])

plt.plot(xpoints_Pillow, ypoints, color = '#ff5c33', marker = 'o')

# Title
plt.title("Pillows Produced Over Time")

#Axis Labels
plt.xlabel("Quantity Produced")
plt.ylabel("Time (in hours)")

plt.show()