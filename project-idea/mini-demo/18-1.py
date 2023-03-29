# Python爬取百度搜索的标题和真实URL
# https://blog.csdn.net/weixin_41025946/article/details/106331530

import requests
import urllib3
from bs4 import BeautifulSoup
import time
import pandas as pd



#从element里面进行分析，可以知道百度会给一个自己加密的Url
def convert_url(url):
    resp = requests.get(url=url,
                        headers=headers,
                        allow_redirects=False, 
                        verify=False
                        )
    return resp.headers['Location']


#获取url    
def get_url(wd,num):
 
    s = requests.session()
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    total_title = []
    total_url = []
    total_info = []

    #第1页为小于10的数字 10为第2页，20为第三页，30为第四页，以此类推
    num = num*10-10
    
    for i in range(-10, num, 10):
        url = 'https://www.baidu.com/s'     # 点击界面第二页可以看到网页变化截取关键部分 https://www.baidu.com/s?wd=python&pn=10 
        params = {
            "wd": wd,
            "pn": i,
        }
        r = s.get(url=url, headers=headers, params=params,verify=False)
        print("返回状态码:",r.status_code)      #可以看对应Js 正常网页访问时候 status状态码 为200
        soup = BeautifulSoup(r.text, 'lxml')

        for so in soup.select('#content_left .t a'):
            g_url = convert_url(so.get('href'))     #对界面获取的url进行进行访问获取真实Url
            g_title = so.get_text().replace('\n','').strip()    #根据分析标题无对应标签 只能获取标签内文字 去掉换行和空格
            print(g_title, g_url)
            total_title +=[g_title]
            total_url +=[g_url]
            
        time.sleep(1 + (i / 10))
        print("当前页码：",(i+10)/10+1)
        
    try: 
        total_info = zip(total_title,total_url)
        df = pd.DataFrame(data=total_info,columns=['标题','Url'])
        df.to_csv("web_data.csv", index=False, encoding='utf_8_sig')
        print("保存成功")
    except:
        print("false")
        return 'FALSE'
    
if __name__ == '__main__':
    while True:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
            "Host": "www.baidu.com",
        }
        wd = input("输入搜索内容：")
        num =int(input("输入页数："))
        get_url(wd,num)

