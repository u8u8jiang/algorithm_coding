

# python 高階函數的應用3     

## Pandas  
初識series類型      
初識dataframe   
重新索引、數學運算和數據對齊    
dataframe和series間的運算和排序     
層次化索引      
dataframe的層次索引的訪問和彙總運算     
pandas讀寫csv文件       
pandas讀取excel文件並畫圖       
matplotlib可視化及學習方法建議      


---

:clap: 為甚麼需要學習pandas?     
因為pandas含有使得數據分析工作變得更快更簡單的高級數據結構和操作工具    
pandas是基於NumPy所構建, 使得以NumPy為中心的應用變得更加簡單.       

```py
# pip install pandas
import pandas as pd
from pandas import Series, DataFrame
```
## 1. 初識series類型
Series類型說明: 類似於一維數組的對象, 是由一組數據 與 一組與之相關的數組標籤組成(索引). 僅由一組數據即可產生最簡單的 Series.     

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

## 2. 初識dataframe     

* DataFrame是一個表格型的數據結構, 含有一組有序的列. 每列可以是不同值的類型、數值、字符串、布爾值...      
* DataFrame本身有行索引, 也有列索引        
* DataFrame可以理解成由series組成的一個字典       

```py
# create a dataframe
data = {
    '60年代':['狗子', '嘎子', '秀兒'],
    '70年代':['衛國', '建國', '愛國'],
    '80年代':['李雷', '韓梅梅', '張偉']
}
frame_data = DataFrame(data)
print(frame_data)
print(frame_data['70年代'])


# create a dataframe about timeseries
import numpy as np
dates = pd.date_range('20190301', periods=6)
print(dates)

df = pd.DataFrame(np.random.rand(6,4), index = dates, columns = list('ABCD'))
print(df)
df.T
df['20190301':'20190303']   #不是左閉右開, 而是兩端包含     

df.loc['20190301':'20190303', ['A','B']]  #對行與列同時進行篩選 
df.at[dates[0], 'A']
df.head(2)
df.tail(3)
```

DataFrame構造函數可接受哪些數據類型呢?  
1. 二維numpy array      
2. 由 數組、列表或元組 組成的字典      
3. 由 Series 組成的字典      
4. 由 字典 組成的字典   
5. 字典或Series的列表
6. 由 列表或元組 組成的列表      
7. 另一個DataFrame  


## 3. 重新索引、數學運算和數據對齊      

pandas 重新索引 reindex     
```py
obj = Series([4.5, 9.8, -1.2], index=['a', 'b', 'c'])
obj1 = obj.reindex(['a', 'b', 'c', 'e', 'f'])
print(obj)
print(obj1)
obj.reindex(['a', 'b', 'c', 'e', 'f'], fill_value=1)    #以1填充空值


obj = Series([4.5, 9.8, -1.2], index=[0, 2, 4])
obj1 = obj.reindex(range(6), method='ffill')    #ffill 前向值填充; bfill 後向值填充
print(obj)
print(obj1)
```

數學運算和數據對齊  
pandas的重要功能, 可對不同索引的對象進行算數運算,       
再將對象相加時, 如果存在不同的索引時, 則結果的索引就是該索引的並集.      

```py
d1 = Series([1.3, 1.5, 2.6, -3.5], index=['a', 'b', 'c', 'd'])
d2 = Series([-1.3, -1.5, -2.6, 3.9, 9.8], index=['a', 'b', 'c', 'd', 'e'])
print(d1+d2)    #不交集索引為空值



df1 = DataFrame(np.arange(9).reshape((3,3)), columns = list('abc'), index = [1,2,3])
df2 = DataFrame(np.arange(12).reshape((4,3)), columns = list('cde'), index = [1,2,3,4])
print("df1")
print(df1)
print("df2")
print(df2)

print("df1 + df2")
print(df1 + df2)
df1.add(df2, fill_value=0)  #用0來填充不重疊的值, 若本身位置為空值, 依然為空值
```


## 4. dataframe和series間的運算和排序  

```py
frame = DataFrame(np.arange(12).reshape((4,3)), columns = list('bde'), index = [1,2,3,4])
series = frame.loc[1]   #選取frame中索引為1的一行數據   

print('frame')
print(frame)
print('series')
print(series)
print('frame - series')
print(frame - series)  #一直向下廣播相減


series = Series(range(3), index = list('bef'))

print('frame')
print(frame)
print('series')
print(series)
print('frame + series')
print(frame + series)  #相加時, 沒有就合併
```

排序: 根據條件對數據集進行排序  

```py
obj = Series(range(4), index=['d','e','a','b'])
print(obj)

obj.sort_index()
obj.sort_values()


# 針對DataFrame, 根據任意一個軸上的索引進行排序 
frame = DataFrame(np.arange(8).reshape((2,4)), index=['two', 'one'], columns=['c', 'd', 'a', 'b'])
frame.sort_index()
frame.sort_index(axis=1)    #指定軸進行排序


frame = DataFrame({'b':[4,7,2,-1], 'a':[0,4,2,0]})
frame
frame.sort_values(by='b')
```

## 5. 層次化索引

層次化索引是pandas的重要功能, 能在一個軸上用有多個索引級別, 另一種說法是 能以低維度形式處理高維度數據.  
```py
data = Series(np.random.randn(10), index = [['a','a','a','b','b','b','c','c','d','d'], 
                                            [1,2,3,4,5,6,7,8,1,2]])
data.index

# 選取子集的操作
data['b']
data['b':'d']

# 內層選取
data[:,2]   #第一層索引選擇所有的元素, 第二層索引中選擇索引為2的元素    

data.unstack()    #以unstack生成新的dataframe
data.unstack().stack()
```

對於dataframe, 每條軸都可以有分層索引, 各層也都可以有名字   
```py
frame_data = DataFrame(np.arange(12).reshape((4,3)),
                        index = [['a','a','b','b'], [1,2,1,2]],
                        columns = [['Black','Yellow','Blue'],['Green','Red','Green']])
print(frame_data)

frame_data.index.names = ['key1', 'key2']
print(frame_data)

frame_data.columns.names = ['color1', 'color2']
print(frame_data)
```

## 6. dataframe的層次索引的訪問和彙總運算   

DataFrame類型層次化索引的操作       

```py
frame_data = DataFrame(np.arange(12).reshape((4,3)),
                        index = [['a','a','b','b'], [1,2,1,2]],
                        columns = [['Black','Yellow','Black'],['Green','Red','Blue']])
print(frame_data)


# dataframe的層次索引的訪問 
frame_data['Black']     #對列進行篩選
frame_data.loc['a', ['Black']]      #行和列同時進行訪問篩選    
```

根據級別彙總統計
```py
#求和運算
frame_data.sum(level='key2')



frame_data = DataFrame(np.arange(12).reshape((4,3)),
                        index = [['a','a','b','b'], [1,2,1,2]],
                        columns = [['Black','Yellow','Black'],['Green','Red','Green']])

frame_data.index.names = ['key1', 'key2']
frame_data.columns.names = ['color1', 'color2']
print("frame_data")
print(frame_data)

#求和運算
print("frame_data.sum(level='color2', axis=1)")
print(frame_data.sum(level='color2', axis=1))
```


## 7. pandas讀寫csv文件       
pandas 文本格式數據處理     
* read_csv: 從文件、url、文件型對象中加載帶分隔符的數據, 默認分隔符為逗號     
* read_table: 從文件、url、文件型對象中加載帶分隔符的數據, 默認分隔符為制表符'\t'   
* read_fwf: 讀取固定寬列格式        
* read_clipboard: 讀取剪貼板中的數據, 可以看做是read_table的剪貼板, 可以用在將網頁中的數據轉換為表格中數據時用到        

```py
pd.read_csv('data.csv')
pd.read_table('data.csv', sep = ',')    #指定分隔符
pd.read_csv('data.csv', header=None)  #沒有表頭, 所有文件中的數據皆為目標數據, 自動生成表頭

pd.read_csv('data.csv', index_col='c')    #指定c列為索引列
pd.read.csv('data.csv', index_col=['c','d'])    #指定多列為層次列
```
```py
pd.read_csv('data2.csv')    #文件中的NA表示為空     
pd.read_csv('data2.csv', skiprows=[1])  #不讀取哪一行   

data = pd.read_csv('data2.csv')
pd.isnull(data)


# 大文件如何讀取    
data = pd.read_csv('data2.csv', nrows=5)

data.to_csv('data3.csv', sep='|')   #改變分隔符作保存   
```


## 8. pandas讀取excel文件並畫圖  

```py
pd.read_excel('data_excel.xlsx')
pd.read_excel('data_excel.xlsx', sheet_name='工作表2')


excel = pd.read_excel('data_excel.xlsx', sheet_name='工作表2')
print(excel)
pl = excel.plot(kind='scatter', x='age', y='place').get_figure()
pl.savefig('1.png')
```
```py
import numpy as np
dates = pd.date_range('20200101', periods=6)
df = pd.DataFrame(np.random.rand(6,4), index=dates, columns=list('ABCD'))
print(df)

pl = df.plot(kind='scatter', x='A', y='B').get_figure()
pl.savefig('2.png')
```

## 9. matplotlib可視化及學習方法建議      

matplotlib可視化    

```py
# pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn


plt.plot(np.arange(10))


# 子圖展示
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

plt.plot(randn(50).cumsum(), 'k--')     #灰色
ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3*randn(30))

# fig.savefig('fig.png')




# other color

# plt.plot(randn(50).cumsum(), 'g--')     #綠色

x = [1,2,3,4,5]
y = [1,2,3,4,5]
plt.plot(x, y, linestyle='--', color='#CECECE')
```

```py
# series畫圖
from pandas import Series, DataFrame

s = Series(randn(10).cumsum(), index=np.arange(0,100,10))
s.plot()

# DataFrame畫圖
df = DataFrame(np.random.randn(10,4).cumsum(0), columns=['A','B','C','D'],
                index = np.arange(0,100,10))
df.plot()


# other plot
# https://matplotlib.org/stable/gallery/index

```

