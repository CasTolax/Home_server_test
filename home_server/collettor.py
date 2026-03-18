#VThe data will be processed here.
#import datetime  -- optional
import psutil

#CPU DATA
def cpu_ctrl(): 

    return {
        "cpu_use": psutil.cpu_percent(1),               # CPU PERCENT
        "cpu_times": psutil.cpu_times(),                # CPU TİMES
        "cpu_cores": psutil.cpu_freq(),                 # CPU frequency
        "cpu_sta": psutil.cpu_stats()._asdict()
    }

cpu_ctrl()

#İNTERNET DATA
def net(): 

    return {
        "net_connection": psutil.net_connections(),     # internet connections data
        "_infoconnection": psutil.net_io_counters(),    # internet Internet data exchange
        "adress_connection": psutil.net_if_addrs()      # internet adress data
    }

net()

#HARDWARE DATA
def hardware(): 

    return {
        "hardware_temp":psutil.sensors_temperatures(),  #  hardware temp
        "hardware_fan":psutil.sensors_fans(),           # fan speed
        "hardware_batt":psutil.sensors_battery(),       # power or battery data
    }

hardware()

#SYSTEM DATA
def _system(): 

    return {
        "sys_boot_time": psutil.boot_time(),            # System boot time
        "sys_user": psutil.users()                      # Users data
    }

_system()



