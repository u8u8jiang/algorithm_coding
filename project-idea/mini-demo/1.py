# 骰子模拟器    
# 目的：创建一个程序来模拟掷骰子。    
# 提示：当用户询问时，使用random模块生成一个1到6之间的数字。        

import random

while int(input('Press interger to roll the dice or 0 to exit:\n')):
    print(random.randint(1, 6))
