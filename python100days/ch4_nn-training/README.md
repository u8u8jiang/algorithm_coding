
## ch4 神經網路的學習    


* 學習是指，從訓練資料開始, 自動取得最適當的權重參數, 以損失函數為基準, 找出最小權重參數.   
* 利用函數的斜率, 找出最小函數值的梯度法    
驅動資料: 從資料中學習的典範轉移       
* 機器學習的核心是資料, 找出某個類型與規則性, 避免人為介入.      
    * 從影像資料擷取**特徵量**, 利用**機器學習**技術思考特徵量類型(SIFT, SURF, HOG), 但必須注意影像轉換為向量時的特徵量, 還是需要由人設計.   
    * **神經網路**從資料中學習, 利用資料, 自動決定權重參數的值. 神經網路面對問題, 會將資料是為未處理資料, 徹底學習取得資料, 找出問題類型.     
#
* 追求模型的一般化能力, 需分為訓練資料與測試資料. 一般化能力, 處理未看見資料的能力, 可對應多個數據集, 避免overfitting.   
* 使用指標為*損失函數(loss function)*, 可使用任意函數, 不過一般主要使用均方誤差與交叉謪誤差.   

```py
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)  

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


# test
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

mean_squared_error(np.array(y1), np.array(t))
mean_squared_error(np.array(y2), np.array(t))
cross_entropy_error(np.array(y1), np.array(t))
cross_entropy_error(np.array(y2), np.array(t))
```

* 小批次學習: 學習過程中, 從訓練資料中選出一部分, 近似為整體資料

```py
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, y_train), (x_test, y_test) = \
load_mnist(normalize=True, one_hot_label=True)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
y_batch = y_train[batch_mask]
```


* 為什麼設定損失函數, 而不用辨識準確度?    
* 因為辨識準確度, 幾乎在所有位置, 微分都會變成0 (似階梯函數)   
* 對多變數函數微分, 稱為*偏微分*. 偏微分與一個變數的微分一樣, 都是計算某個位置的斜率, 準確來說, 偏微分是在多個變數中, 鎖定成目標的某一變數, 其他變數固定成某個數值.    
* 同時進行全部變數的偏微分, 稱為 *梯度gradient*   


```py
import numpy as np

# recall: 數值微分(numerical differentiation)
def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h)-f(x-h))/(2*h)

# recall: 梯度gradient
def numerical_gradient(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)
    
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)  # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x)  # f(x-h)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val  # 恢復原值

    return grad


# test
# let f(x0,x1) = x_0**2 + x_1**2

def fu(x):
    return x[0]**2 + x[1]**2

def fu_tmp1(x0):
    return x0*x0 + 4.0**2.0
a = numerical_diff(fu_tmp1, 3.0)

def fu_tmp2(x1):
    return 3.0**2.0 + x1*x1
b = numerical_diff(fu_tmp2, 4.0)

c = numerical_gradient(fu, np.array([3.0, 4.0]))

print(a, b, c)

```


梯度法
* 梯度法, 反覆往梯度方向移動找函數極值.    
* 找最小值稱為 *梯度下降法(gradient descent method)* .梯度是在各個地點, 指出減少最多函數值的地方, 但無法保證為函數最小值   

學習率(learning rate)
* 決定在一次學習中要學習多少, 更新多少參數. 可以設{0.01, 0.01...}等某一數值, 值太大或太小都無法到達適當位置.     
* 學習率太大, 會往大數值擴展；學習率太小, 幾乎不會更新就結束.   
* 超參數(hyperpaeameter) vs 一般參數(權重&偏權值)? 一般參數, 是根據訓練資料與學習演算法, 自動獲得的參數. 超參數是人工設定的參數.           

```py
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        gred = numerical_gradient(f, x)
        x -= lr * gred

    return x

# test
init_x = np.array([-3.0, 4.0])
gradient_descent(fu, init_x=init_x, lr=0.1, step_num=100)
```

> /gradient_simplenet.py   
* 形狀2*3的權重參數   
```py
class simpleNet:
...

# test
net = simpleNet()
print("net.w: ", net.W)

x = np.array([0.6, 0.9])
p = net.predict(x)
print("p= ", p)

t = np.array([0, 0, 1])   #label
loss = net.loss(x, t)
print("loss= ", loss)

f = lambda w: net.loss(x, t)
dW = numerical_gradient(f, net.W)
print("dW= ", dW)
```

## 小結: 執行學習演算法   
:triangular_flag_on_post: 小批次, 計算梯度, 更新參數, 重複   
* 前提: 神經網路有適合的權重與偏權值, 為了符合訓練資料, 而調整權重與偏權值, 稱為 "學習".   
* **Step1. 小批次:** 從訓練資料隨機挑選部分資料, 挑選出的資料稱為 "小批次". 階段目標為- 減少小批次的損失函數.   
* **Step2. 計算梯度:** 為了減少小批次的損失函數, 計算各權重參數的梯度, 梯度會顯示 損失函數值減少最多的方向.   
* **Step3. 更新參數:** 權重參數只往梯度方向微量更新.    
* **Step4. 重複**
    * 這邊使用的資料是隨機挑選 作為小批次, 又稱為 stochastic gradient descent(SGD).   

> /two_layer_net.py   
* def init, predict, loss, accuracy, numerical_gradient
* init: 權重是按照常態分佈的亂數進行初始化   
* def gradient: 誤差反向傳播法,  vs to numerical_gradient(self, x, t)-使用數值微分算參數的梯度, gradient(self, x, t)-可較快得到結果.   

```py
class TwoLayerNet:
...

# test

net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
a1 = net.params['W1'].shape     #(784, 100)
a2 = net.params['b1'].shape     #(100,), 第一層的偏權值   
a3 = net.params['W2'].shape     #(100, 10)
a4 = net.params['b2'].shape     #(10)
print(a1, a2, a3, a4)

# forward, 推論處理(正向處理)  
x = np.random.rand(100, 784)   #虛擬的輸入資料  
y = net.predict(x)
t = np.random.rand(100, 10)    #虛擬的label   

grads = net.numerical_gradient(x, t)
b1 = grads['W1'].shape     #(784, 100)
b2 = grads['b1'].shape     #(100,), 第一層的偏權值   
b3 = grads['W2'].shape     #(100, 10)
b4 = grads['b2'].shape     #(10)
print(b1, b2, b3, b4)
```

> /train_neuralnet.py    
* 假設小批次=100, 每次從 60,000 筆訓練資料中隨機抽取100筆資料    
    * 接著 計算梯度, 利用準確度SGD更新參數, 重複(iteration)10,000次   
    * 每次更新, 計算訓練資料的損失函數, 將值新增在list中   
    * 用圖表顯示損失函數變化    
* 隨著學習次數增加, 損失函數逐漸減少, 表示權重逐漸適應資料
* 每1 epoch計算所有訓練資料與測試資料的辨識準確度, 並且記錄結果.  
    * 為甚麼每 1 epoch為單位計算辨識準確度?   
    * 因為若是在for中紀錄, 很花時間. 
    * 隨著epoch提升, 辨識準確度皆提升, 且兩條線幾乎重疊, 表示沒有過度學習.        

```py
a = np.arange(len(train_loss_list))
plt.plot(a, train_loss_list, label='loss')
plt.show()
```
