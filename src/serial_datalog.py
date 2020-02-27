import sys
import os
import argparse
import serial
import time # Optional (if using time.sleep() below)


parser = argparse.ArgumentParser(description='Receive data from serial and display it in hex')
parser.add_argument('-i', '--interface', required=True, help='Interface to communicate with.')

args = vars(parser.parse_args())
print("Interface: ", format(args["interface"]))


tty_port = args["interface"]

try:
	ser = serial.Serial( port=tty_port,
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
except serial.SerialException as e:
	print ("Port {} unavailable serial device", tty_port)
	sys.exit()

while (True):
    # NB: for PySerial v3.0 or later, use property `in_waiting` instead of function `inWaiting()` below!
    if (ser.inWaiting()>0): #if incoming bytes are waiting to be read from the serial input buffer
        in_bin = ser.read(ser.inWaiting()) #read the bytes,  format binary array
        print(in_bin, end='\t') #print the incoming string without putting a new-line ('\n') automatically after every print()
        print(hex(int.from_bytes(in_bin,byteorder='big')))
    #Put the rest of your code you want here
    time.sleep(0.01) # Optional: sleep 10 ms (0.01 sec) once per loop to let other threads on your PC run during this time. 

ser.close()    