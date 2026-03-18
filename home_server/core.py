#The code, what it does, and the printing process are all here. However, if desired, it can be integrated into your computer.

import os           #The operating system
import sys          #access the system
import datetime     #info date 
import time         #loop, or etc
import json         #file and stroge
import pathlib      #read,write and delete file
import psutil       #sistem info

#required local libraries
from collettor import cpu_ctrl,net,hardware,_system   #data 

 #-- #! -- SCHEDULER MODULE MAYBE İS NOT WORKİNG, PLEASE TESTİNG --

# -- EXAMPLE --
#def deneme():
#    cpu_data = cpu_ctrl()
#    net_data = net()
#    hardware_data = hardware()
#    system_data = _system()
#    print(cpu_data,net_data,hardware_data,system_data)
#deneme()
# -- EXAMPLE --


# -- THERE İS NOT MODULE,SHOULD BE HAVE A PROBLEM --
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
