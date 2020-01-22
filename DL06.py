from pyModbusTCP.client import ModbusClient
import time
from tkinter import *
from subprocess import call
import sys
SERVER_HOST = "192.168.72.114" # whatever you set the IP of your PLC to.  You need to set that up with software that comes with PLC
SERVER_PORT = 502

#have to adjust to fit your screen likely this won't work for other sizes.   Using a 1280x720 screen
h=5 # Height
w=10 #width


c = ModbusClient()
c.host(SERVER_HOST) #192.168.72.114
c.port(SERVER_PORT)


root=Tk()  
root.attributes("-fullscreen",True) #fullscreen
#root.geometry("1280x720") #windowed for debugging

def quitpython():
    exit()

def shutdownraspi():
    call("sudo nohup shutdown -h now", shell=True) # strictly works on raspbian or regular linux to shut down
def RelayTrigger(ADDR): # take in the address
    toggle = True
    print(ADDR)
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

    if c.is_open():
        is_ok = c.write_single_coil(ADDR, toggle) #give 2049 - 2057 a test as well, should trigger Y outputs if not rung to anything
        time.sleep(1)
        toggle = not toggle
        is_ok = c.write_single_coil(ADDR, toggle)


buttonPADC1010=Button(root, height=h, width=w, font =("Helvetica","40"),text="C1010", command=lambda: RelayTrigger(3593))
buttonPADC1010.place(x=30,y=80)

buttonPADC1005=Button(root, height=h, width=w,font =("Helvetica","40"), text="C1005", command=lambda: RelayTrigger(3590))
buttonPADC1005.place(x=430,y=80)

SHUTITALLDOWN=Button(root, height=2, width=w,font =("Helvetica","20"), text="Shut Down", command=lambda: shutdownraspi())
SHUTITALLDOWN.place(x=560,y=400)

QUITPYTHON=Button(root, height=2, width=w,font =("Helvetica","20"), text="Quit Python", command=lambda: quitpython())
QUITPYTHON.place(x=30,y=400)
