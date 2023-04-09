import pyttsx3


class RobotSay():

    def __init__(self):
        # 初始化语音
        self.engine = pyttsx3.init()  # 初始化语音库

        # 设置语速
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', self.rate - 50)


    def say(self, msg):
        # 输出语音
        self.engine.say(msg)  # 合成语音
        self.engine.runAndWait()
        
# robotSay = RobotSay()
# robotSay.say("你好呀")					#会讲出    ~你好呀(女声)
