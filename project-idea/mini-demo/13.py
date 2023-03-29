#  有声读物     
# 目的：编写一个Python脚本，用于将Pdf文件转换为有声读物。       
# 提示：借助pyttsx3库将文本转换为语音。
# 安装：pyttsx3，PyPDF2     


import pyttsx3, PyPDF2
from PyPDF2 import PdfReader

reader = PdfReader(r'./data/test.pdf')
speaker = pyttsx3.init()

for page_num in range(len(reader.pages)):
    page = reader.pages[page_num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()