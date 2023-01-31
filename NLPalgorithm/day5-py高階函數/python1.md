
# python 高階函數的應用     

lambda 表達式   
map函數的應用   
filter過濾器        
reduce 函數     
python三大推導式    
閉包        
裝飾器      


----


## 1. lambda 表達式     
又被稱為匿名函數,   
格式  lambda 參數列表: 函數體

```py
def add(x, y):
    return x + y
print( add(3,4) )

# 調用
add_lambda = lambda x, y : x+y
add_lambda(3,4)
```
```py  
## 三元運算符 
condition = True
print(1 if condition else 2)

condition = False
print(1 if condition else 2)
```

## 2. map函數的應用    

```py
list1 = [1,2,3,4,5]
r = map(lambda x: x+x, list1)
print(list(r))

m1 = map(lambda x, y : x * x + y, [1,2,3,4,5], [1,2,3,4,1])
print(list(m1))

```

## 3. filter過濾器      

```py
def is_not_none(s):
    return s and len(s.strip()) > 0
list2 = [' ', '', 'hello', 'greedy', None, 'ai' ]
result = filter(is_not_none, list2)
print(list(result))

```

## 4. reduce 函數

```py
from functools import reduce    
f = lambda x, y : x + y
r = reduce(f, [1,2,3,4,5], 10) # set initial value is 10
print(r)
```


## 5. python三大推導式      
(1) 列表推導式, 根據已有的列表推導出新的列表    
```py
list1 = [1,2,3,4,5,6]
f = map(lambda x: x+x, list1)
print(list(f))

list2 = [i + i for i in list1]
print(list2)

list3 = [i**3 for i in list1]
print(list3)

list4 = [i*i for i in list1 if i>3] #選擇性篩選 
print(list4)
```
(2) 集合推導式, 根據已有的集合推導出新的集合        
```py
list1 = {1,2,3,4,5,6}
list2 = {i + i for i in list1}
print(list2)

list3 = {i**3 for i in list1}
print(list3)

list4 = {i*i for i in list1 if i>3} #選擇性篩選 
print(list4)
```
(3) 字典推導式      
```py
s = {
    "zhangsan": 20,
    "lisi": 15,
    "wangwu": 31
}
# 拿出所有的key, 並變成列表
s_key = [key for key, value in s.items()]
print(s_key)

# key 和 value顛倒
s1 = {value: key for key, value in s.items()}
print(s1)

# 只拿出符合條件的值
s2 = {key: value for key, value in s.items() if key=="lisi"}
print(s2)
```


##  6. 閉包     
一個返回值是函數的函數      
```py
import time
def runtime():
    def now_time():
        print(time.time())
    return now_time
f = runtime()
# f()
```
```py
# cat data.csv
# 讀出一個文件中帶有某個關鍵字的行
def make_filter(keep):              #keep=8
    def the_filter(file_name):      #file_name = data.csv
        file = open(file_name)      #打開文件
        lines = file.readlines()    #讀取所有文件內容
        file.close()
        filter_doc = [i for i in lines if keep in i]  #過濾文件
        return filter_doc
    return the_filter

filter1 = make_filter("8")  #這一行調用了make_filter函數, 接受了 the_filter函數作為返回值, 
# 也就是說這裡的 filter1 等於函數 the_filter

filter_result = filter1("data.csv")
# print(filter_result)
```

## 7. 裝飾器, 裝飾器, 註解    

```py
# 獲取函數運行的時間    

import time

def runtime(func):
    def get_time():
        print(time.time())
        func()
    return get_time

@runtime
def student_run():
    print("學生跑")

student_run()
```
```py
# 如果函數有參數怎麼解決
# 有參數的裝飾器

import time

def runtime(func):
    def get_time(*args):
        print(time.time())
        func(*args)
    return get_time

@runtime
def student_run(i):
    print("學生跑")
@runtime
def student_run1(i,j):
    print("學生跑1")

student_run(1)
student_run1(1,2)
```

```py
# 關鍵字參數

import time

def runtime(func):
    def get_time(*args, **kwargs):
        print(time.time())
        func(*args, **kwargs)
    return get_time

@runtime
def student_run(i,j):
    print("學生跑")

@runtime
def student_run1(*args, **kwargs):
    print("學生跑1")

@runtime
def student_run2():
    print("學生跑2")

student_run(1,2)
student_run1(5, i = 1, j=2)
student_run2()
```

ex. 開發一個語法糖, 實現參數的類型準確性    
在python中, 大家都知道python的數據類型是弱類型, 比如說函數只允許傳字符串.   
