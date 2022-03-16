import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,20, 0.1)
print(x)

plt.plot(x, x)
plt.plot(x,2*x)
plt.plot(x, np.sin(x)*10+10)
plt.show()
