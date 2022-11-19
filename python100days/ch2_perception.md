

## ch2 Perception 感知器
理論上...
* 機器學習是指決定參數；   
* 人類執行的是, 思考感知器的結構, 給予電腦學習資料.     
* 只要組合反與閘, 就能製作出電腦.  
=> 使用雙層感知器即可製作電腦   
ie. 在活化函數中, 使用非線性的sigmoid函數, 便可表現出任意函數.      


  
> :computer: 從感知器到神經網路...  
##  ch3 神經網路

* 設定符合期待的輸入與輸出之權重, 仍以人工方式進行.   
* 「感知器」是指一種演算法, 指的是單層網路中, 使用活化函數的 *階梯函數 Step function* 之模型. (階梯函數: 把臨界值作為分界轉換輸出的函數)     
* 「多層感知器」一般是指神經網絡. 多層, 使用 *sigmoid函數* 等活化函數的網路.     
* 在神經網路中, 活化函數(sigmoid fu) 轉換訊號, 轉換後的訊號會傳給下一個神經元. 感知器與神經網路, 主要差別於活化函數, 其餘的如神經網路連接多層結構, 訊號的傳遞方法 皆相同.      



```py

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

```

* stepfu and sigmoid 差別在平滑度, 兩形狀相似, 如果輸入是重要訊息, 則輸出較大的值；若輸入訊息較不重要, 則輸出較小的值.  
* 不論輸入多大或多小, 輸出訊號皆會介於0~1之間.   
* 皆為非線性函數. -> think: 為甚麼不使用線性函數?   

```py
# ReLU function
def relu(x):
    return np.maximum(0,x)
# maximum: 從輸入值中, 選取較大的值輸出   
```
sigmoid函數 是最早使用的函數, 而最近較常使用的是ReLU   
若超過0, 則會直接輸出；若0以下, 則輸出0   

>  :computer: 利用numpy運算多維陣列, 再執行神經網路.   

```py
# recall: 多維陣列

import numpy as np

A = np.array([1, 2, 3, 4])
print(A)
np.ndim(A)
A.shape     #tuple  
A.shape[0]

B = np.array([[1,2], [3,4], [5,6]])
print(B)
np.ndim(B)
B.shape     #tuple  


# recall: dot product 矩陣乘積
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])
np.dot(A,B)


A = np.array([[1,2,3], [4,5,6]])
B = np.array([[1,2], [3,4], [5,6]])
np.dot(A,B)   #矩陣A行=矩陣B列


```


```py

## 執行三層的訊息傳遞  

# 輸入層到第一層
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

# print(X.shape)
# print(W1.shape)
# print(B1.shape)

A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1) #通過活化函數, sigmoid fu


# 第一層到第二層
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)


# 第二層到輸出層
# 執行過程與前面相同, 僅最後的活化函數與隱藏層不同.   
def identity_fu(x):
    return x

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z3, W3) + B3
Y = identity_fu(A3)

```

* 隱藏層的活化函數 h(x), 輸出層的活化函數 sigma(x) 
* 輸出層的活化函數, 回歸問題-恆等函數, 分類問題-sigmoid_fu, 多分類問題-softmax_fu     

```py

## 統一執行處裡 
import numpy as np

def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network

def sigmoid(x):
    return 1/(1 + np.exp(-x) )
def identity_fu(x):
    return x


def forward(netwark, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3'] 
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_fu(a3)

    return y


network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)
    
```
* init_network()進行權重與偏權值的初始化, 並儲存在字典型態的network中.    
* forward(), 統一執行 把輸入訊號轉換成輸出的流程   
* others also have "backward", 即輸出往輸入方向的處理.     

```py
## 輸出層設計

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y 
# 如上設計, 容易溢位


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)  #防範溢位
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y    

```
* softmax輸出和為1, 因此softmax的輸出可以視為 對應類別的機率   
* 因為其為單調函數, 輸出最大神經元的位置不變, 因此在進行分類時, 可以省略輸出層的softmax函數.   
* 解決機器學習問題, 步驟可以分為"學習"與"推論"兩階段, 一開始利用學習階段學習模型, 接著在推論階段, 使用學習過的模型, 對未知的資料禁行推論. 推論階段一般會省略softmax函數   

## ch3_mnist dataset  