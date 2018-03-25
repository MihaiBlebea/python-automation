import schedule
import time
import os

def job():
    print("I'm working...")

def send_email():
	os.system("python3 enail_sender.py")


schedule.every(10).minutes.do(send_email)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)