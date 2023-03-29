# 天气应用      
# 目的：编写一个Python脚本，接收城市名称并使用爬虫获取该城市的天气信息。        
# 提示：你可以使用Beautifulsoup和requests库直接从谷歌主页爬取数据。     
# 安装：requests，BeautifulSoup     

from bs4 import BeautifulSoup
import requests


def getHTMLText(url):
    try:
        r = requests.get(url,timeout=10)
        r.raise_for_status()        #确认编码方式
        r.encoding = r.apparent_encoding        #编码
        return r.text       #返回获取网页文本
    
    except Exception as e:
        print(e)
        return ""
    
def buildList(ulist,html):
    soup = BeautifulSoup(html,"lxml")
    lis = soup.select("ul[class='t clearfix'] li")
    for li in lis:
        try:
            date = li.select('h1')[0].text
            weather = li.select('p[class="wea"]')[0].text
            temp = li.select('p[class="tem"] span')[0].text + "/" + li.select('p[class="tem"] i')[0].text
            win = li.select('p[class="win"] i')[0].text
            data = [date,weather,temp,win]
            ulist.append(data)
        except Exception as e:
            print(e)
    
def showList(ulist):
    split = "{0:^10}\t{1:{4}^10}{2:{4}^10}\t{3:^10}"
    isplit = "{0:^10}\t{1:{4}^10}\t{2:{4}^10}\t{3:{4}^10}"
    print(split.format("时间","天气","温度","风量",chr(12288)))
    for list in ulist:
        print(isplit.format(list[0],list[1],list[2],list[3],chr(12288)))


if __name__ == '__main__':
    ulist = []
    city_num = int(input("input the city number "))   #101030100
    url = f"http://www.weather.com.cn/weather/{city_num}.shtml"
    html = getHTMLText(url)
    buildList(ulist,html)
    showList(ulist)
