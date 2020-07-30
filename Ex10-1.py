import numpy as np
import matplotlib.pyplot as plt

x=5
print(np.square(x))
theta = 45
print(np.sin(theta))
print(np.cos(theta))
meshPoints=np.linspace(-1,1,500)
print(meshPoints[53])
plt.plot(meshPoints,np.sin(2*np.pi*meshPoints))
plt.show()
