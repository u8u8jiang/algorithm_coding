

# 辨識手寫數字   
* 使用學習完的參數, 執行神經網路的推論處理. 這種推論處理, 又稱為神經網路的正向傳播(forward propagation).   
* 和解決機器學習步驟一樣, 使用神經網路解問題時, 一開始也要使用訓練資料進行權重學習, 推論時使用學習過的參數, 將輸入資料進行分類.   


```py
# MNIST dataset
import sys, os
sys.path.append(os.pardir)   #載入父目錄檔案設定
from dataset.mnist import load_mnist

(x_train, y_train), (x_test, y_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
```

dataset/mnist.py     
* 先載入父目錄檔案設定, 接著載入dataset/mnist.py的load_mnist函數, 再接著載入load_mnist函數, 讀取MNIST資料集.    
* load_mnist(flatten, normalize): flatten=true, 儲存為一行numpy形式, 顯示影像時需reshape為28*28的大小； nomalize=true, 考量資料整體分布的預處理, 將影像各像素值除以225, 範圍在0~1間.    
* 另外, 其他預處理手法, whitening, 讓整個資料分布形狀均勻一致.   

mnist_show.py    
* from PIL import Image: 另外當作numpy儲存的影像資料, 需轉為PIL用的資料物件, 但這邊轉換需利用Image.formarray()進行.     

neuralnet_mnist.py        # inferance process     
* 輸入層28*28=784, 輸出層10個數字, 隱藏層有兩個-第一層50個, 第二層100個    
* sample_weight.pkl儲存學習完畢的權重值, 儲存為字典型態的變數     
* accuracy: 評估辨識準確度, 確認是否能正確分類.   
* 最初取得MNIST資料集, 產生網路. 接著用for逐一取出x的影像資料, 利用predit()分類, 輸出numpy. 接著從機率清單, 取最大值得索引值. 最後, 預測值與正確值比對, 將正確答案的比例作為辨識準確度.   

neuralnet_mnist_batch.py
* 在神經網路運算中, 傳送資料形成瓶頸時進行批次處理, 可以減少匯流排頻寬的負擔. (precisely, 增加載入資料時的運算比例.)     


```py
x, t = get_data()
network = init_network()

batch_size = 100     #batch
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))
```
