import time
import schedule

def hello():
    print('Hello world')

job = schedule.every(10).seconds.do(hello)
# schedule.cancel_job(job)

while True:
    schedule.run_pending()
    time.sleep(1)
