import time
import datetime
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


# 阻塞调用
# scheduler = BlockingScheduler()
# 后台调用
scheduler = BackgroundScheduler()


def run_once():
    print(f'run_once @ {datetime.datetime.now()}')

run_date = datetime.datetime.now()+datetime.timedelta(seconds=10)
job = scheduler.add_job(run_once, 'date', run_date=run_date)
print('scheduler start...')
scheduler.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break
