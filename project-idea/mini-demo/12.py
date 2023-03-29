# 闹钟      
# 目的：编写一个创建闹钟的Python脚本。      
# 提示：你可以使用date-time模块创建闹钟，以及playsound库播放声音。      

from datetime import datetime
from playsound import playsound     

alarm_time = input("Enter the time of alarm to be set: HH:MM:SS \n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8] 
alarm_period = alarm_time[9:11].upper()

print(alarm_hour, alarm_minute, alarm_seconds, alarm_period)
print("Setting up alarm...")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S") 
    current_period = now.strftime("%p")
    # print(current_hour, current_minute, current_seconds, current_period)

    
    if (alarm_period==current_period):
        if (alarm_hour==current_hour):
            if (alarm_minute==current_minute):
                if (alarm_seconds==current_seconds):
                    print("Wake up!")
                    playsound(r"./data/house_lo.mp3")
                    break
                





