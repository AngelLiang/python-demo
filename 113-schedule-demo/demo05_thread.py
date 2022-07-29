import time
import schedule
from threading import Thread

def task1():
    print('Hello task1')


class ScheduleThread(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.job = schedule.every(3).seconds.do(task1)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)


# daemon=True: 设置为后台运行
t = ScheduleThread(daemon=True)
t.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass



