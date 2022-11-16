

import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x>0, dtype=np.int)

def sigmoid(x):
    return 1/(1 + np.exp(-x) )


x = np.arange(-5.0, 5.0, 0.1)
y1 = step_function(x)
y2 = sigmoid(x)

plt.plot(x, y1, label="stepfu")
plt.plot(x, y2, linestyle="--", label="sigmoid")
plt.ylim(-0.1, 1.1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("stepfu & sigmoid")
plt.legend()
plt.show()







