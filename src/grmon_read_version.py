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
# Get  version value.
#data = struct.pack(">BBBBB", 128, 255, 242,10,8)
rd_rtr_ver = b'\x80\xFF\xF2\x0A\x08'
ser.write(rd_rtr_ver)
s = ser.read(4)
print(s)


time.sleep(1)
en_spw1 = b'\xC0\xFF\xF2\x08\x04\x00\x14\x00\xFE'
ser.write(en_spw1)

time.sleep(1)
rd_rtr_status = b'\x80\xFF\xF2\x08\x84'
ser.write(rd_rtr_status)
s = ser.read(4)
print(s)
#Disable the SpaceWire 2 interface 0x0C 0xFFF20808 0x001404F0
#dis_spw2 = struct.pack(">BBBBBBBBB", 192, 255, 242,8,8,0,14,4,240)
#ser.write(dis_spw2)


#Configure the SIST port
# Address 1.
time.sleep(1)
cfga_addr0_sist = b'\xC0\xFF\xF2\x02\x00\x01\x00\x00\x00'
ser.write(cfga_addr0_sist)

# Config  Seed
time.sleep(1)
cfga_seed_sist = b'\xC0\xFF\xF2\x02\x24\x00\x01\x00\x01'
ser.write(cfga_seed_sist)

# Packet Length
time.sleep(1)
cfg_len_sist  = b'\xC0\xFF\xF2\x02\x28\x00\x00\x00\x0F'
ser.write(cfg_len_sist)

# Sist control
time.sleep(1)
#cfg_ctrl_sist  = b'\x81\x01\xF2\x02\x28\x00\x00\x00\x0F'
#ser.write(cfg_ctrl_sist)



#MBA address Register Acronym
#0xFFE00200 - 0xFFE0021C SpaceWire Address Register 0-7 SIST.ADDR0 - SIST.ADDR7
#data = struct.pack(">BBBBBBBBB", 192, 255, 242,8,4,0,14,4,240)


#0xFFE00220 Protocol ID and Polynomial Register SIST.PID
#0xFFE00224 Seed Register SIST.SEED
#0xFFE00228 Packet Length Register SIST.LEN
#0xFFE0022C Control Register SIST.CTRL
#0xFFE00230 Error Register 0 SIST.ERROR0
#0xFFE00234 Error Register 1 SIST.ERROR1
#0xFFE00238 Error Register 2 SIST.ERROR2
#0xFFE0023C Packet Counter Register SIST.PKTCNTR
#0xFFE00240 Timer Register 0 SIST.TIMER0
#0xFFE00244 Timer Register 1 SIST.TIMER1
#0xFFE00248 Status Register SIST.STAT
#0xFFE0024C State Register SIST.STATE
#0xFFE00250 Transmitter Byte Count Register SIST.TXBYTECNTR
#0xFFE00254 Receiver Byte Count Register SIST.RXBYTECNTR
#0xFFE00258 Time-Code Register SIST.TIME
#0xFFE0025C Protection Register SIST.PROT
#0xFFE00280 - 0xFFE0029C (multiple mapping) Data Input Registers 0-7 SIST.DIN
#0xFFE002A0 - 0xFFE002BC (multiple mapping) Data Output Registers 0-7 SIST.DOUT



ser.close()

