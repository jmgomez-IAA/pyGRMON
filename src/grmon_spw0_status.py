import serial
import struct
import time

ser = serial.Serial( port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

print(ser.isOpen())
# Allow the device to synchronize the baudrate of the UART
data = struct.pack(">B", 85)
ser.write(data)

time.sleep(2)

rd_rtr_status = b'\x80\xFF\xF2\x08\x84'
ser.write(rd_rtr_status)
s = ser.read(4)
print(s)

time.sleep(1)
rd_rtr_config = b'\x80\xFF\xF2\x08\x04'
ser.write(rd_rtr_config)
s = ser.read(4)
print(s)

ser.close()

