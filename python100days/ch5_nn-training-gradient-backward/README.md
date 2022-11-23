

## ch5 誤差反向傳播法 (backward propagation)      

* 上一章: 神經網路權重參數的梯度, 是利用數值微分計算.   
* 反向傳播: 對節點的輸入訊號, 乘上局部性微分(偏微分), 再傳遞給下一節點. 由連鎖率構成.  

```py
# 乘法層
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y                
        out = x * y

        return out

    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x
        
        return dx, dy
```

```py
#  加法層
class AddLayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y

        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        
        return dx, dy
```
整合運用:  buy_apple_orange.py  
   
   
   

## :jack_o_lantern: 執行活化函數層   
* 把構成神經網路的 層layer 當作一個類別執行, 首先執行 ReLU, Sigmoid layer

> common/layers.py
```py
## ReLU- Rectified Linear Unit  
class Relu:
...

## Sigmoid function
class Sigmoid: 
...
```


* 執行Affine & Softmax layer

```py
# recall: 多維陣列運算   
X = np.random.rand(2)
W = np.random.rand(2,3)
B = np.random.rand(3)

Y = np.dot(X, W) + B


# Affine Transformation 仿射轉換   
class Affine:

    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)

        return dx
```
* Softmax-with-Loss layer   
* 神經網路分為推論與學習兩階段, 在推論階段, 可以直接用最後的affine層輸出作為辨識結果, 未必需要用到softmax層。而在學習階段，會需要用到softmax層.    
* 以交叉謪誤差作為softmax函數的損失函數，進行反向傳播，可以導出 (y1-t1, y2-t2, y3-t3) 的整齊結果。    
ie. 在回歸問題中, 於輸出層使用 "恆等函數", 以及 以"均方誤差"作為損失函數, 的原因在此.     
ie. 使用均方誤差作為 "恆等函數" 的損失函數時, 反向傳播會得到 (y1-t1, y2-t2, y3-t3) 的整齊結果.    

```py
class SoftmaxWithLoss:
...
```
* 反向傳播, 必須注意到 以 batch_size 除以傳播值, 將每個資料的誤差傳遞上一層.   


## :jack_o_lantern: 執行誤差反向傳播法   

**神經網路的學習總圖**     

* **前提:**  神經網路具有可適應的權重與偏權值, 調整權重與偏權值, 以適應訓練資料, 這種過程稱作 "學習". 神經網路的學習可以分成：     
* **步驟1 小批次:**   從訓練資料中, 隨機取出部分資料.    
* **步驟2 計算梯度:**  計算與各權重參數有關的損失函數梯度. :star: 反向傳播是這個步驟       
* **步驟3 更新參數**  往梯度方向微量更新權重參數.    
* **步驟4 重複** 

**:pushpin: 執行對應誤差反向傳播法的神經網路**   
> two_layer_net.py
* TwoLayerNet: 使用"層級"傳播, 就能達到處理辨識結果 **predict()**, 計算梯度 **gradient()** 的目的.  
* 使用 OrderedDict 有序字典, 按順序新增到字典. 正向傳播, 按順序呼叫各層的forward(); 反向傳播, 按相反方向呼叫各層. 按順序連結各層.   
* **模組化**：把神經網路的構成 以"層"為單位, 只要增加必要層級 即可製作較大網絡. 
> train_neuralnet.py
* 誤差反向傳播法計算梯度  


**誤差反向傳播法的梯度確認**
* 計算梯度的方法: 數值微分, 反向傳播   
* 數值微分計算時間多於反向傳播, 其優點是執行過程簡單, 較不容易發生錯誤. 反之, 反向傳播計算較為複雜, 所以較容易發生問題. 因此,    
:star: 經常利用數值微分, 確認反向傳播是否正確執行.   

> gradient_check.py   
* 計算數值微分算出來的梯度 與 誤差反向傳播法的結果 所產生的誤差.   


```py
# 計算梯度
grad_numerical = network.numerical_gradient(x_batch, t_batch)
grad_backprop = network.gradient(x_batch, t_batch)


# 計算各權重的絕對誤差平均值
for key in grad_numerical.keys():
    diff = np.average( np.abs(grad_backprop[key] - grad_numerical[key]) )
    print(key + ":" + str(diff))
```
