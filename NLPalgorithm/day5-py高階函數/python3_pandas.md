

# python 高階函數的應用3     
pandas  
為甚麼需要學習pandas?     
因為pandas含有使得數據分析工作變得更快更簡單的高級數據結構和操作工具    
pandas是基於NumPy所構建, 使得以NumPy為中心的應用變得更加簡單.       

```py
# pip install pandas
import pandas as pd
from pandas import Series, DataFrame
```
## Series類型說明: 
類似於一維數組的對象, 是由一組數據 與 一組與之相關的數組標籤組成(索引). 僅由一組數據即可產生最簡單的 Series.     

```py
obj = Series([1,2,3,4,5])
print(obj)
print(obj.values)
print(obj.index)


# 自定義索引
obj = Series(['a', 'b', 'c', 'd', 'e'], index=[1,2,3,4,5])
print(obj)
obj[2]

# 也可以把Series當字典使用  
data = {'a':10000, 'b':20000, 'c':30000}
obj = Series(data)  #此時, Series中的索引是字典中的鍵       
print(obj)
keys = ['a', 'c']
obj1 = Series(data, index=keys)
print(obj1)

# 缺失數據的處理        
data = {'a':None, 'b':20000, 'c':30000}
obj = Series(data)       
print(obj)

pd.isnull(obj)
pd.notnull(obj)


# 缺失數據的處理 
data = {'LiLei':None, 'HanMeimei':25, 'Tony':None, 'Jack':50}
odj = Series(data)
obj.name = 'NameAndAge'
obj.index.name = 'Xingming' #指定索引名稱
print(obj)

```




```py


```





