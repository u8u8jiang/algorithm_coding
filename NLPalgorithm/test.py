

import pandas as pd
from pandas import Series, DataFrame

# 缺失數據的處理 
data = {'LiLei':None, 'HanMeimei':25, 'Tony':None, 'Jack':50}
obj = Series(data)
print(obj)
obj.name = 'NameAndAge'
obj.index.name = 'Xingming'
print(obj)



