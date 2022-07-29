import time
import schedule

def task1():
    print('Hello task1')

job = schedule.every(3).seconds.do(task1)
# schedule.cancel_job(job)

def task2():
    print('Hello task2')

job = schedule.every(5).seconds.do(task2)
schedule.cancel_job(job)


while True:
    schedule.run_pending()
    time.sleep(1)
