

import numpy as np
import matplotlib.pyplot as plt

position = 0
walk = [position]   #步值初始化
steps = 1000    #步數設置   

for i in range(steps):
    step = 1 if np.random.randint(0,2) else -1
    position += step
    walk.append(position)

plt.plot(walk)
print((np.abs(walk)>10).argmax())