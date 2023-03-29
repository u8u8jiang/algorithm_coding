# 故事生成器
# 目的：每次用户运行程序时，都会生成一个随机的故事。    
# 提示：random模块可以用来选择故事的随机部分，内容来自每个列表里。  

import random

when = ["A few years", "Yesterday", "Last night", "A long time ago", "On 20th Jan"]
who = ["a rabbit", "an elephant", "a mouse", "a turtle", "a cat"]
name = ["Ali", "Miriam", "Daniel", "Hoouk", "Starwalker"]
residence = ["Barcelona", "India", "Germany", "Venice", "England"]
went = ["cinema", "university", "seminar", "school", "laundry"]
happened = ["made a lot of friends", "ate a hamburger", 
            "found a secret key", "solved a mistery", "wrote a book"]

print(random.choice(when) + ',' + 
      random.choice(who) + ' that lived in ' + random.choice(residence) + 
      ', went to the ' + random.choice(went) + 
      ' and ' + random.choice(happened))


