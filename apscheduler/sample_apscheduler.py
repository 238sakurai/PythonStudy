from apscheduler.scheduler import Scheduler
import datetime
import time

def job_function_13sec():
    print datetime.datetime.today()
    time.sleep(13)
    print "Hello World"

sched = Scheduler(standalone=True,coalesce=True)
sched.add_interval_job(job_function_13sec, seconds=10)
sched.start()
