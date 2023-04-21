'''
本接口即将停止更新，请尽快使用Pro版接口：https://tushare.pro/document/2     
quary 股票訊息      

'''

import tushare as ts
import pandas as pd 

data = ts.get_hist_data("601318", "2017-01-01", "2020-01-10")       
print(data)             


data.close[::-1].plot(figsize=(16,8), kind="line")      
