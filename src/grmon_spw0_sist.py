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
#Configure the SIST port

#Enable
# Enable SIST PORT on SIST PROT.
time.sleep(1)
en_sist = b'\xC0\xFF\xE0\x02\x5C\x55\xAA\x00\x01'
ser.write(en_sist)

# Enable SIST PORT on SIST PROT.
time.sleep(0.5)
en_sist = b'\x80\xFF\xE0\x02\x5C'
expected = b'\x55\xAA\x00\x01'
ser.write(en_sist)
s = ser.read(4)
print("1.0 Enable sist port", "Expected:", expected, "Value",  s)

# Enable SIST PORT on RTR PCTRL (Remove disable bit)
# Reset FIFOs and enable Configuration Port Access, Disable = 0.
time.sleep(1)
en_port_sist = b'\xC0\xFF\xF2\x08\x4C\x00\x00\x00\xC4'
ser.write(en_port_sist)

# Enable SIST PORT on SIST PROT.
time.sleep(1)
en_port_sist = b'\x80\xFF\xF2\x08\x4C'
expected = b'\x00\x00\x00\xC4'
ser.write(en_port_sist)
s = ser.read(4)
print("1.0 Enable sist port", "Expected:", expected, "Value",  s)


#Packet Config

# Address 1.
time.sleep(1)
cfga_addr0_sist = b'\xC0\xFF\xE0\x02\x00\x01\x00\x00\x00'
ser.write(cfga_addr0_sist)

# Config  Protocol
time.sleep(1)
cfga_pid_sist = b'\xC0\xFF\xE0\x02\x20\x00\x2D\x00\xF0'
ser.write(cfga_pid_sist)

# Config  Seed
time.sleep(1)
cfga_seed_sist = b'\xC0\xFF\xE0\x02\x24\x00\x01\x00\x01'
ser.write(cfga_seed_sist)

# Packet Length
time.sleep(1)
cfg_len_sist  = b'\xC0\xFF\xE0\x02\x28\x00\x00\x00\x0F'
ser.write(cfg_len_sist)

# Reset timers
time.sleep(1)
cfg_timer0_sist  = b'\xC0\xFF\xE0\x02\x40\x00\x00\x00\x00'
ser.write(cfg_timer0_sist)
time.sleep(1)
cfg_timer1_sist  = b'\xC0\xFF\xE0\x02\x44\x00\x00\x00\x00'
ser.write(cfg_timer1_sist)

#Check packet structure before transmit.
time.sleep(1)
packet_addr = b'\x80\xFF\xE0\x02\x00'
packet_pid  = b'\x80\xFF\xE0\x02\x20'
packet_seed = b'\x80\xFF\xE0\x02\x24'
packet_len  = b'\x80\xFF\xE0\x02\x28'
time.sleep(0.5)
ser.write(packet_addr)
addr = ser.read(4)
time.sleep(0.5)
ser.write(packet_pid)
pid = ser.read(4)
time.sleep(0.5)
ser.write(packet_seed)
seed = ser.read(4)
time.sleep(0.5)
ser.write(packet_len)
leng = ser.read(4)
print("2.0 Packet:", addr, pid, seed, leng)

# Sist control
time.sleep(1)
cfg_ctrl_sist  = b'\xC0\xFF\xE0\x02\x2C\x81\x09\x00\x01'
ser.write(cfg_ctrl_sist)



# Read reaming bytes to transfer
time.sleep(1)
sist_txbytecntr = b'\x80\xFF\xE0\x02\x50'
ser.write(sist_txbytecntr)
s = ser.read(4)
print("3.0 reaming bytes",  s)
ser.close()

