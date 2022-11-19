


# MNIST dataset
import sys, os
sys.path.append(os.pardir)   #載入父目錄檔案設定
from dataset.mnist import load_mnist

(x_train, y_train), (x_test, y_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)