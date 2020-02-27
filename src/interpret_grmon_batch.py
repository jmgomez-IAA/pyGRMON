import sys
import os
import argparse
import serial
from binascii import unhexlify
import struct
import time


def uart_send(data):
	b = ser.write(data)


def send_write_cmd (cmd, addr, data):
	#Compose the command
	cmd_bytes = cmd+addr+data	
	uart_send(cmd_bytes)

def send_read_cmd (cmd, addr):
	#Compose the command
	cmd_bytes = cmd+addr	
	print (cmd_bytes)
	uart_send(cmd_bytes)
	s = ser.read(4)
	print("SIST port status", s)


# Addapt the input to conver from hex.
# The number of digits should be pair.
# Remove 0x from the strings
# Remove Spaces.
def parse_hex(hex_str):
	try:
		raw_hex = hex_str.lstrip("0x")
		hex_bytearray = bytearray.fromhex(hex_str[2:])
		return (hex_bytearray)

	except ValueError as e:
		print ("Error converting : {}\n".format(hex_str))	

def parse_cmd(cnt, cmd_file):
	if cmd_file.startswith('#') : return

	if cmd_file.startswith('wmem') :
		cmd, addr, val = cmd_file.rstrip("\n").split()
		#Let build a bayte array from addr and val.		
		print(" {} \t|\t {} {} {}".format(cnt, cmd, addr, val))

		cmd_data = b'\xC0'
		addr_data = parse_hex(addr)
		val_data = parse_hex(val)

		# Debug
		#print (addr_data)
		#print (val_data)

		send_write_cmd (cmd_data, addr_data, val_data)
		

	if cmd_file.startswith('mem') :	
		cmd, addr = cmd_file.split()
		print(" {} \t|\t {} {}".format(cnt, cmd, addr))
		cmd_data = b'\x80'
		addr_data = parse_hex(addr)
		send_read_cmd (cmd_data, addr_data)
		# Debug
		#print (addr_data)		

parser = argparse.ArgumentParser(description='Executes the commands of a TCL script wi')
parser.add_argument('-i', '--interface', required=True, help='Interface to communicate with.')
parser.add_argument('-s','--script', required=True, help='GRMON script to execute')

args = vars(parser.parse_args())


print("Interface: ", format(args["interface"]))
print("Script: ", format(args["script"]))


tty_port = args["interface"]
tcl_script = args["script"]

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


ser.isOpen()
sync_data = b'\x55\x55'
print (sync_data)	
ser.write(sync_data)
print ("Port is opened.")

time.sleep(0.100)

with open(tcl_script) as cmd_file:
	for cnt, line in enumerate(cmd_file):		
		parse_cmd(cnt, line)
		time.sleep(0.010)

ser.close()
