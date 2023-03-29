#  随机密码生成器   
# 目标：创建一个程序，可指定密码长度，生成一串随机密码。    
# 提示：创建一个数字+大写字母+小写字母+特殊字符的字符串。根据设定的密码长度随机生成一串密码。   

import random
passlen = int(input("Enter the length of password"))
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
psw = "".join(random.sample(s, passlen))
print(psw)