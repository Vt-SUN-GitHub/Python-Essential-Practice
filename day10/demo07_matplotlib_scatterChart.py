import matplotlib.pyplot as plt
import numpy as np
from day10.funcLibrary import randomColor
rand = np.random.randint(0,100,size=(1000,2))

plt.scatter(rand[:,0], rand[:,1], s=40, c=randomColor(), alpha=0.5, marker="v")
plt.show()

