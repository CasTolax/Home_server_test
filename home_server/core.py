#Kodun nasıl davrancağı, ne gibi durumlarda kapanıp,
#açılacağı ve sistem açıldığında kontrol edilecek şeyler vb.

import os           #işletim sisteminin dosya yolu ve dosya okuma-yazdırma
import sys          #sisteme erişim için
import datetime     #zaman bilgisi
import time         #uyu,saniye tut işlemleri
import json         #dosyalama ve veri depolama
import pathlib      #dosya yolu,dosyalama işlemi-yazdırma-okuma
import psutil       #Sistem bilgisi

#yerel gerekli kütüphaneler
from collettor import cpu_ctrl,net,hardware,_system   #veri 

#import scheduler#depolama    #zaman -- #! -- SCHEDULER MODULU CORE MODULUNU CALISTIRMIYOR --

# -- ÖRNEK --
#def deneme():
#    cpu_data = cpu_ctrl()
#    net_data = net()
#    hardware_data = hardware()
#    system_data = _system()
#    print(cpu_data,net_data,hardware_data,system_data)
#deneme()
# -- ÖRNEK --


# -- MODUL YOK ÖRNEK --
#def control_module():

#        try:
#            import psutil
#        except ModuleNotFoundError:
#              raise SystemExit(
#                    "Gerekli bağımlılık eksik: 'psutil' kurulu değil.\n"
#                    "kurmak için: pip install psutil"  
#                )
    
#control_module()


def coll_data():

    cpu_data = cpu_ctrl()
    net_data = net()
    hardware_data = hardware()
    sys_data = _system()

    all_data = [cpu_data,net_data,hardware_data,sys_data]

    with open("data.json","w",encoding="utf-8") as f:
        json.dump(all_data,f,indent=2,ensure_ascii=False)
        
    
coll_data()
