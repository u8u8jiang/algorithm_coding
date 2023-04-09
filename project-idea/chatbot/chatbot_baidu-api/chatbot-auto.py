import urllib.parse
import requests
from pyaudio import PyAudio, paInt16
from RobotSay import RobotSay
from speak import Speak
from ReadWav import ReadWav


def talkWithRobot(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["content"]


robotSay = RobotSay()
speak = Speak()
readTalk = ReadWav()
while True:

    speak.my_record()                               #录音

    text = readTalk.predict()['result'][0]          #调用百度AI接口, 将录音转化为文本信息

    print("本人说:", text)                           #输出文本信息
    response_dialogue = talkWithRobot(text)         #调用青云客机器人回答文本信息并返回
    print("青云客说:", response_dialogue)             #输出回答文本信息

    robotSay.say(response_dialogue)                 #播放回答信息
