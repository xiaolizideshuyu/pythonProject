import time
from rich.progress import track

for i in track(range(3), description="进度..."):
    time.sleep(0.5) # 模拟执行任务耗费的时间

track(range(5,16), description="进度...",
        complete_style="green", finished_style="green")

if __name__ == '__main__':
    track(range(5,6))