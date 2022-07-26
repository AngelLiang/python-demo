import datetime
import time

import schedule

def job():
    print(f"I'm working... at {datetime.datetime.now()}")

# 每隔 10s 运行1次
schedule.every(10).seconds.do(job)
# 每隔 10m 运行1次
schedule.every(10).minutes.do(job)
# 每小时运行1次
schedule.every().hour.do(job)
# 每天 10:30 运行1次
schedule.every().day.at("09:48").do(job)
schedule.every(5).to(10).minutes.do(job)
# 每周一运行一次
schedule.every().monday.do(job)
# 每周三13:15运行一次
schedule.every().wednesday.at("13:15").do(job)
# schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
# schedule.every().minute.at(":17").do(job)


def job_with_argument(name):
    print(f"I am {name}")


schedule.every(10).seconds.do(job_with_argument, name="Peter")

while True:
    schedule.run_pending()
    time.sleep(1)
