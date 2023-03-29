#  文字冒险游戏     
# 目的：编写一个有趣的Python脚本，通过为路径选择不同的选项让用户进行有趣的冒险。    

name = str(input("Enter your name\n"))
print(f"{name} you are stuck in a forest. Your task is to get out from the forest without dieing")
print("You are walking threw forest and suddenly a wolf come in your way. Now you have two options.")
print("1. Run 2. Climb the nearest tree")

user = int(input("Choose one option 1 or 2 "))
if user==1:
    print("Your died!!")
elif user==2:
    print("You survived!!")
else:
    print("Incorrect input")

