

## Perception 感知器
理論上...
* 機器學習是指決定參數；   
* 人類執行的是, 思考感知器的結構, 給予電腦學習資料.     
* 只要組合反與閘, 就能製作出電腦.  
=> 使用雙層感知器即可製作電腦   
ie. 在活化函數中, 使用非線性的sigmoid函數, 便可表現出任意函數.      


  
> :computer: 從感知器到神經網路...  
##  神經網路

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

