#Every minute,record time and stroge with json,.
import time
import datetime
import json
from pathlib import Path

time_of_log = Path("time_of_log.json")      # record

def datenow_data():

    while True:
        local_time_now = {
            "local_time": datetime.datetime.now().isoformat()           # Get the local time, save it, and convert it to ISO format
        }
        
        # write file
        with time_of_log.open("a",encoding="utf-8") as f:
            f.write(json.dumps(local_time_now,ensure_ascii=False)+"\n")
            print("kayıt ediliyor...")
            time.sleep(60)                                             # wait a one minute
       
datenow_data()
