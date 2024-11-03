import os

import uiautomator2 as u2
import time
import random

# 连接手机：选择有线或无线的连接方式

d = u2.connect()  # connect to device via USB
# d = u2.connect('192.168.31.6:37027')  # connect to device via wifi
print(d.info)  # check connection


# 定义刷抖音的动作
def watch_douyin_hours(hours=24):  # default to watch for 24 hours

    # open app
    d(text="抖音极速版").click()
    time.sleep(2)
    n = 0
    start = time.perf_counter()  # returns the float value of time in seconds

    # start watching
    while True:
        d.swipe(0.5, 0.8, 0.6, 0.3, 0.2)
        n += 1
        os.system(f'adb shell screencap -p /sdcard/screenshots/' + str(n) + '.jpg') #截图保存到手机
        os.system(f'adb pull /sdcard/screenshots/' + str(n) + '.jpg') #传到电脑上
        sleepTime = random.randint(5, 12)
        print(f'已刷完第{n}个视频,随机等待{sleepTime}秒')
        time.sleep(10 + sleepTime)
        total_time = time.perf_counter() - start
        if (total_time > hours * 3600):
            break

    print("Watched ", n, "videos in ", hours, "hours")
    return (n)


# 开始刷抖音，并记录刷过的视频数
if __name__ == '__main__':
    n = watch_douyin_hours(24 * 31 * 365)  # choose to watch for 2 hours
    print(n)
