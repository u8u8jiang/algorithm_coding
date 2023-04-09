# 请求智能机器人, 发送文本信息, 返回智能聊天内容    
# 一个免费、无需注册、只需要发送get请求就可实现聊天的青云客智能机器人，直接调用接口即可

import urllib.parse
import requests


def talkWithRobot(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["content"]

print(talkWithRobot("你好呀!"))

