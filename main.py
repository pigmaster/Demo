__author__ = 'phil'

from threading import Thread
from time import sleep
import serial
from serial.tools import list_ports
import os

def logger():
    a = 0
    while(True):
        sleep(1)
        a += 1
        print a

def printer():
    b=1000
    while(True):
        sleep(2)
        b += -1
        print b

def serial_ports():
    """
    Returns a generator for all available serial ports
    """
    if os.name == 'nt':
        # windows
        for i in range(256):
            try:
                s = serial.Serial(i)
                s.close()
                yield 'COM' + str(i + 1)
            except serial.SerialException:
                pass
    else:
        # unix
        for port in list_ports.comports():
            if "USB" in port[0]:
                yield port[0]



if __name__ == "__main__":

    # Initializing Serial Ports

    print(list(serial_ports()))
    com_port = '/dev/ttyUSB0'
    list_com_ports = list(serial_ports())

    
    while (any(com_port in s for s in list_com_ports)):
        com_port = str(raw_input("What COM Port to connect to: "))
    try:
            ser = serial.Serial(port = com_port, baudrate = 9600,timeout = 1) #port = "/dev/ttyS30"
    except IOError as e:
        print "I/O Error - Could not connect to COM Port".format(e.errno, e.strerror)
    # Creating Child Threads
    #thread1 = Thread(target = logger)
    #thread2 = Thread(target = printer)
    #thread1.start()
    #thread2.start()
