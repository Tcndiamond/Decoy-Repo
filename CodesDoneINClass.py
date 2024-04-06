import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 5, step = 0.01)
y = 3*np.sin(4*np.pi*t)

plt.figure()
plt.plot(t,y)
plt.xlabel("Time in seconds")
plt.ylabel("Amplitude")
plt.title("Sinewave of 2Hz")
plt.show()

#Hi
