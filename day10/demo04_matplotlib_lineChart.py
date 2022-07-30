import matplotlib.pyplot as plt
import numpy as np

#折线图
x = np.arange(0,2*3.14,0.01)
y = np.sin(x)
plt.plot(x, y, 'b:')
plt.show()


