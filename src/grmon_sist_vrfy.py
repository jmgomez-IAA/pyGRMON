import serial
import struct
import time

ser = serial.Serial( port='/dev/ttyUSB1',
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
#Configure the SIST port

#Enable the SIST port on pctrl
time.sleep(1)
en_pctrl_sist = b'\xC0\xFF\xF2\x08\x4C\x00\x10\x80\x20'
ser.write(en_pctrl_sist)

time.sleep(0.4)
rd_pctrl_sist = b'\x80\xFF\xF2\x08\x4C'
ser.write(rd_pctrl_sist)
s = ser.read(4)
print("SIST port control reg", s)

# Read the status register
time.sleep(0.4)
rd_status_sist = b'\x80\xFF\xF2\x08\xCC'
ser.write(rd_status_sist)
s = ser.read(4)
print("SIST port status", s)

#Enable
# Enable SIST PORT on SIST PROT.
time.sleep(1)
en_sist = b'\xC0\xFF\xE0\x02\x5C\x55\xAA\x00\x01'
ser.write(en_sist)

time.sleep(0.3)
en_sist = b'\x80\xFF\xE0\x02\x5C'
expected = b'\x55\xAA\x00\x01'
ser.write(en_sist)
s = ser.read(4)
print("1.0 Enable sist port")
print("\tExpected:", expected)
print("\tRead Value:",  s)


ser.close()

