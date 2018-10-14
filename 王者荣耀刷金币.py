import os
import time
frequency=0
money=19
while True:
    os.system('adb shell input tap {} {}'.format(1780,970))#再次挑战
    time.sleep(3)
    os.system('adb shell input tap {} {}'.format(1600,970))#闯关
    time.sleep(80)
    os.system('adb shell input tap {} {}'.format(1780,970))#点击屏幕
    time.sleep(3)
    frequency+=1
    print("刷了{0}次{1}金币".format(frequency,frequency*money))
