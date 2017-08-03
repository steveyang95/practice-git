from datetime import datetime
import time

def printTime():
    print(datetime.now().strftime('%H:%M:%S'))
    time.sleep(5.0)

for i in range(6):
    printTime()
