# Hangman       
# 目的：创建一个简单的命令行hangman游戏。       
# 提示：创建一个密码词的列表并随机选择一个单词。现在将每个单词用下划线“_”表示，给用户提供猜单词的机会，如果用户猜对了单词，则将“_”用单词替换。      

import time
import random

name = input("What is your name? ")
print("Hello, "+ name, "time to play hangman! ")
time.sleep(1)
print("Start guessing...\n")
time.sleep(0.5)

# a list of secret words    
words = ["python", "programming", "treasure", "creative", "medium", "horror"]
word = random.choice(words)
guesses = ""

turns = 5
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed +=1
    if failed == 0:
        print("\n you won")
        break
    
    guess = input("\n guess a character: ")
    guesses += guess

    if guess not in words:
        turns -=1
        print("\n wrong")
        print("\n you have", + turns, "more guesses")
        if turns == 0:
            print("\n you lose")

