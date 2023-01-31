
# python 高階函數的應用2     


numpy基礎       
numpy數組的創建     
numpy的矢量化運算       
numpy的花式索引     
numpy數組轉置和軸對換       
條件邏輯轉數組      
數學運算與排序      
numpy文件處理       
線性代數函數和隨機漫步例子      

---

## 1. numpy基礎
numpy(seris) 的外面是pandas(dataframe)      
numpy 其實是一個多維的數組對象      

```py
import numpy as np

data = [1,2,3,4,5]
n = np.array(data * 10)
print(data)
print(n)

# 每個np數組, 皆有shape和dtype的屬性
print(n.shape)    # 表獲取np數組的維度(長度)
print(n.dtype)    # 表獲取np數組的類型
```

## 2. numpy數組的創建       

嵌套序列: 是由一組等長列表組成的列表
```py
arr = [[1,2,3,4], [1,2,3,4]]
arr2 = np.array(arr)
print(arr2)

print(arr2.ndim)    # ndim表維度
print(arr2.shape)
```
np對數據類型的判斷
```py
# 不好的示範
arr = [['1','2',3,4], [5,6,7,8]]
arr2 = np.array(arr)
print(arr2)
print(arr2.dtype)    # unicode類型, 即numpy裡的字符串

# integer
arr = [[1,2,3,4], [5,6,7,8]]
arr2 = np.array(arr)
print(arr2)
print(arr2.dtype)    

# float
arr = [[1.1,2,3,4], [5,6,7,8]]
arr2 = np.array(arr)
print(arr2)
print(arr2.dtype)    #當其一元素為float時, 會自動推斷為float64類型
```
numpy進行指定長度數組的創建     
```py
np.zeros(10)
np.ones((2,3))
np.empty((2,3,4))

np.arange(10)   # arange是range函數的數組版本

arr = np.array([1.2, 1.6, 1.8, -2.3, -5.8])
print(arr)
print(arr.dtype)
print(astype(np.int32))     # 轉換數據類型
```

int類型 8 16 32 64      
float類型 16 32 64 128   
- float16 半精度浮點數, float32 標準單精度浮點數, float64 標準雙精度浮點數, float128 擴展精度浮點數       

## 3. numpy的矢量化運算     
矢量化: 數組不用透過編寫循環, 即可進行批量運算
```py
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr1 + arr2

# 兩對相同數量的數組運算
arr1 = np.array([[1,2,3,4], [1,2,3,4]])
arr2 = np.array([[5,6,7,8], [9,6,7,8]])

arr1 + arr2
arr1 * arr2
arr1 - arr2
arr1 / arr2
```
```py
# 標量值會傳播 broadcast
arr1 = np.array([[1,2,3,4], [10,2,3,4]])
5 * arr1
```

## 4. numpy的花式索引  

numpy數組的索引和切片操作   
```py
arr = np.arange(10)
print(arr)
print(arr[1])

print(arr[4:])  #切片從第4個元素到最後

arr[0:4] = 11   #標量賦值於切片
print(arr)

array_copy = arr.copy()
print(array_copy)
```

二維數組的訪問方式      
```py
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1[0][1])
print(arr1[0,1])    #兩種方式對於數組是等價的


names = np.array(['Tony', 'Jack', 'Robin'])
print(names == 'Tony')
print((names == 'Tony') & (names == 'Robin'))   #AND操作
print((names == 'Tony') | (names == 'Robin'))   #OR操作
```

花式索引(Fancy Indexing)     
numpy中, 利用整數數組進行索引       
```py
arr = np.empty((8,4))
# print(arr)

for i in range(8):
    arr[i] = i
print(arr)      # 賦值

print(arr[[4,3,0,6]])   
#以一個特定的順序選取行中的子集, 我們傳入一個用於指定順序的整數列表, 或數組
#這裡也可以用負數索引從末尾獲取
print(arr[[-2,-1,3,6]])
```

```py
arr = np.arange(32).reshape((8,4))
# print(arr)


# 為array的切片操作, 屬於廣播型 

print("原本reshape後的數組")
print(arr[[1,5,7,2]])

print("先進行 行篩選, 再篩選每行的數值")
print(arr[[1,5,7,2],[0,3,1,2]])

print("先選取1572行數據, 再選取0312順序列")
print(arr[[1,5,7,2]][:,[0,3,1,2]])

print("依造 列選擇, 得到相同的結果")
print(arr[np.ix_([1,5,7,2],[0,3,1,2])])
```

## 5. numpy數組轉置和軸對換     

數組轉置和軸對換    
轉置為重塑數組的一種特殊形式, 常用的方法 T和 transpose  

```py
arr = np.arange(15).reshape((3,5))
print("一個3*5的矩陣")
print(arr)
print("一個3*5的矩陣, 做了個轉置")
print(arr.transpose())
print("轉置的另一種表示方式")
print(arr.T)


arr = np.arange(24).reshape((2,3,4))
print("一個2*3*4的矩陣")
print(arr)
print("一個2*3*4的矩陣, 做了軸與軸的轉置, 即3個面間的切換")
# 軸0: 3*4的面； 軸1: 2*4的面； 軸2: 2*3的面
print("arr.transpose((1,2,0))=")
print(arr.transpose((1,2,0)))
print("arr.transpose((1,0,2))=")
print(arr.transpose((1,0,2)))
```

## 6. 條件邏輯轉數組    
np.where 等同於 python中的 x if condition else y  矢量化的版本      
x if condition else y , 當條件condition成立時, 表達式的返回值為x, 不成立時則為y     
np.where的寫法, 一般用於一個數組產生另一個新數組, 與python的 map, reduce等函數相似.  
```py
x_arr = np.array([1.1, 1.2, 1.3])
x_arr = np.array([2.1, 2.2, 2.3])
condition = np.array([True, False, True])
result = [(x if c else y) for x, y, c in zip(x_arr, y_arr, condition)]

# zip 接受的參數是可迭代的對象  
# zip() 用於將可迭代的對象作為參數, 將對象中對應的元素包成一個個元組, 然後返回這元組組成的列表  
print(result)


r = np.where(condition, x_arr, y_arr)
print(r)    #與result結果一樣, 為矢量化表示的一種形式  

```

```py
# 值替換    
arr = np.random.randn(4,4)
print(arr)
arr1 = np.where(arr>0, 2, -2)
print(arr1)
arr2 = np.where(arr>0, 2, arr)
print(arr2)
```

## 7. 數學運算與排序      
numpy的數學運算     
常用函數 sum mean std       

```py
arr = np.random.randn(4,4)
print(arr)
print(arr.mean())  
print(np.mean(arr))     #一樣的結果

print(arr.sum())
print(arr.std())


# 單一軸上的運算    
print(arr.mean(axis=1))     #計算軸1上的平均值
print(arr.sum(0))       #計算軸0上的和

# argmin  argmax  cumsum
```
排序方法    
```py
arr = np.random.randn(4)
print(arr)
arr.sort()      #從小到大進行排序
print(arr)

# 多維數組排序  
arr = np.random.randn(4,4)
print(arr)
arr.sort(1)      #傳遞軸號, 按軸進行排序
print(arr)
arr.sort(0)      #傳遞軸號, 按軸進行排序
print(arr)
arr.sort()
print(arr)
```

## 8. numpy文件處理    
numpy的文件操作     
numpy可讀寫磁盤上的文本數據, 或二進制數據, 主要應用的函數是 np.save 和 np.load, 默認情況下數據是以未壓縮的原始二進制格式保存在 副檔名為.npy的文件中.    
```py
# 1- 保存為文件
arr = np.arange(10)
# print(arr)
np.save('any_array', arr)
np.load('any_array.npy')

# 2- 保存為壓縮文件        
arr = np.arange(10)
np.savez('any_array_1', a=arr)  #保存為一個壓縮文件, 數組以關鍵字參數的形式傳入     
np.load('any_array_1.npz')['a']

# 3- 保存為壓縮文件, 有無後綴都無妨        
arr = np.arange(10)
np.savez('any_array_2.npz', a=arr)
np.load('any_array_2.npz')['a']
```
```py
# 4- 保存為txt文本
arr = np.arange(10)
np.savetxt('any_array.txt', arr, delimiter=',') #保存為txt文本, 分隔符指定為逗號
np.loadtxt('any_array.txt', delimiter=',')
```

## 9. 線性代數函數和隨機漫步例子      
線性代數        
dot     矩陣的乘法運算      
trace   計算對角線元素的和      
det     計算矩陣行列式      
eig     計算矩陣的evale, evector        
inv     計算矩陣的逆矩陣        

```py
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,2],[4,5],[7,8]])
print(x.dot(y))
```

隨機漫步的例子      
```py
import numpy as np
import matplotlib.pyplot as plt

# 求甚麼時候第一次距離初始點10步遠    
position = 0
walk = [position]   #步值初始化
steps = 1000    #步數設置   

for i in range(steps):
    step = 1 if np.random.randint(0,2) else -1
    position += step
    walk.append(position)

plt.plot(walk)
print((np.abs(walk)>10).argmax())
```


