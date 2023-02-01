
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

s = Series(randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()
