#Veriler burada toplanıp işlenecek.
#import datetime  -- opsiyonel
import psutil

#İŞLEMCİ DEĞERLERİ
def cpu_ctrl(): #işlemci bilgi

    return {
        "cpu_use": psutil.cpu_percent(1),               # işlemci kullanım yüzdesi
        "cpu_times": psutil.cpu_times(),                # işlemci saat hızı
        "cpu_cores": psutil.cpu_freq(),                 # işlemci istatiksel gösterim
        "cpu_sta": psutil.cpu_stats()._asdict()
    }

cpu_ctrl()

#İNTERNET DEĞERLERİ
def net(): #internet bilgi

    return {
        "net_connection": psutil.net_connections(),     # internet değerleri
        "_infoconnection": psutil.net_io_counters(),    # internet veri alış-veriş
        "adress_connection": psutil.net_if_addrs()      # internet adres bilgisi
    }

net()

#DONANIM DEĞERLERİ
def hardware(): #donanım bilgi

    return {
        "hardware_temp":psutil.sensors_temperatures(),  #  Sıcaklık
        "hardware_fan":psutil.sensors_fans(),           # Fan hızı ve marka
        "hardware_batt":psutil.sensors_battery(),       # Güç-şarj
    }

hardware()

#SİSTEM DEĞERLERİ VE BİLGİ
def _system(): #sistem bilgi

    return {
        "sys_boot_time": psutil.boot_time(),            # Sistem boot süresi
        "sys_user": psutil.users()                      # Kullanıcı bilgisi, örn -> isim
    }

_system()



