#Her dakika da bir kere json dosyasına lokal zamanı kayıt eder.
import time
import datetime
import json
from pathlib import Path

time_of_log = Path("time_of_log.json")      # kaydın alınacağı yer

def datenow_data():

    while True:
        local_time_now = {
            "local_time": datetime.datetime.now().isoformat()           # yerel zamanı al ve iso formatına çevir
        }
        
        #Dosya ya yazdır
        with time_of_log.open("a",encoding="utf-8") as f:
            f.write(json.dumps(local_time_now,ensure_ascii=False)+"\n")
            print("kayıt ediliyor...")
            time.sleep(60)                                             # 1 dakika bekle
       
datenow_data()
