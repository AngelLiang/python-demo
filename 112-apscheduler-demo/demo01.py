import time
import datetime
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


# 阻塞调用
# scheduler = BlockingScheduler()
# 后台调用
scheduler = BackgroundScheduler()


def hello():
    print(f'hello @ {datetime.datetime.now()}')

job = scheduler.add_job(hello, 'interval', seconds=3)
print('scheduler start...')
scheduler.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break
