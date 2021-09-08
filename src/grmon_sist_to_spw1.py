import serial
from binascii import unhexlify
import struct
import time

ser = serial.Serial( port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)


ser.isOpen()


# Allow the device to synchronize the baudrate of the UART
data = struct.pack(">B", 85)
ser.write(data)

time.sleep(2)
#Configure the SIST port


############################################################
# Phase 1: Reset SIST, Reset GR718B, Enable Spw1 port.
############################################################
# 1.0  SW reset the SIST via SIST.PROT.RST bit
time.sleep(.500)
#wmem 0xffe0025c 0x55aa0040   
rst_sist = b'\xC0\xFF\xE0\x02\x5C\x55\xAA\x00\x40'
ser.write(rst_sist)

# 1.1 SW reset the complete router via RTR.RTRCFG.RE bit
#wmem 0xfff20a00 0x9002c183 
time.sleep(.500)
rst_gr718b = b'\xC0\xFF\xF2\x0A\x00\x90\x02\xC1\x83'
ser.write(rst_gr718b)

# 1.2 Enable Spw1 port by setting RTR.OCDTRLx.RD=1,RTR.PCTRLx.LD=0 and RTR.PCTRLx.DI=0
# Spw Port 1
#wmem 0xfff20804 0x011c802E  
time.sleep(.500)
en_spw1 = b'\xC0\xFF\xF2\x08\x04\x01\x1c\x08\x2E'
ser.write(en_spw1)

# 2.0 Clearing spw port 1 counters
# Out char counter
# wmem 0xfff20c10 0xffffffff  
time.sleep(.500)
clr_out_char_cntr = b'\xC0\xFF\xF2\x0C\x10\xFF\xFF\xFF\xFF'
ser.write(clr_out_char_cntr)
# In char counter
# wmem 0xfff20c14 0xffffffff  
time.sleep(.500)
clr_in_char_cntr = b'\xC0\xFF\xF2\x0C\x14\xFF\xFF\xFF\xFF'
ser.write(clr_in_char_cntr)
# Out packet counter
# wmem 0xfff20c18 0xffffffff  
time.sleep(.500)
clr_out_pck_cntr = b'\xC0\xFF\xF2\x0C\x18\xFF\xFF\xFF\xFF'
ser.write(clr_out_pck_cntr)
# In packet counter
# wmem 0xfff20c1c 0xffffffff 
time.sleep(.500)
clr_in_pck_cntr = b'\xC0\xFF\xF2\x0C\x1c\xFF\xFF\xFF\xFF'
ser.write(clr_in_pck_cntr)


# 2.1 Clearing sist port counters
# Out char counter
# wmem 0xfff20d30 0xffffffff  
time.sleep(.500)
clr_out_char_cntr = b'\xC0\xFF\xF2\x0D\x30\xFF\xFF\xFF\xFF'
ser.write(clr_out_char_cntr)
# In char counter
# wmem 0xfff20d34 0xffffffff
time.sleep(.500)
clr_in_char_cntr = b'\xC0\xFF\xF2\x0D\x34\xFF\xFF\xFF\xFF'
ser.write(clr_in_char_cntr)
# Out packet counter
# wmem 0xfff20d38 0xffffffff
time.sleep(.500)
clr_out_pck_cntr = b'\xC0\xFF\xF2\x0D\x38\xFF\xFF\xFF\xFF'
ser.write(clr_out_pck_cntr)
# In packet counter
# wmem 0xfff20d3c 0xffffffff
time.sleep(.500)
clr_in_pck_cntr = b'\xC0\xFF\xF2\x0D\x3c\xFF\xFF\xFF\xFF'
ser.write(clr_in_pck_cntr)


# 2.2 Clearing error bits
#wmem 0xfff20884 0x0000a01f 
time.sleep(.500)
clr_err_psts1 = b'\xC0\xFF\xF2\x08\x84\x00\x00\xA0\x1F'
ser.write(clr_err_psts1)

# 2.3 Clearing all SIST.ERROR registers
#wmem 0xffe00230 0x00000000  
time.sleep(.500)
clr_err1_sist = b'\xC0\xFF\xE0\x02\x30\x00\x00\x00\x00'
ser.write(clr_err1_sist)

#wmem 0xffe00234 0x00000000  
time.sleep(.500)
clr_err2_sist = b'\xC0\xFF\xE0\x02\x34\x00\x00\x00\x00'
ser.write(clr_err2_sist)

#wmem 0xffe00238 0x00000000  
time.sleep(.500)
clr_err3_sist = b'\xC0\xFF\xE0\x02\x38\x00\x00\x00\x00'
ser.write(clr_err3_sist)


# 2.4 enable ports SPW1 and SIST
##############################
#wmem 0xfff20804 0x0010002e  
time.sleep(.500)
en_spw1_pctrl = b'\xC0\xFF\xF2\x08\x04\x00\x10\x00\x2E'
ser.write(en_spw1_pctrl)

#wmem 0xfff2084c 0x00008020 
time.sleep(.500)
en_sist_pctrl = b'\xC0\xFF\xF2\x08\x4C\x00\x00\x80\x20'
ser.write(en_sist_pctrl)

#wmem 0xfff209cc 0xc000de00  
time.sleep(.500)
en_sist_pctrl2 = b'\xC0\xFF\xF2\x09\xCC\xC0\x00\xDE\x00'
ser.write(en_sist_pctrl2)

# 2.5 Configuratino status 
# wmem 0xfff20a00 0x00000100 
time.sleep(.500)
cfg_reg = b'\xC0\xFF\xF2\x0A\x00\x00\x00\x01\x00'
ser.write(cfg_reg)


# 2.6 Interrup Mask
###############

# Interrupt on invalid address Mask
# wmem 0xfff20a18 0x00000004  
time.sleep(.500)
enia_mask_int = b'\xC0\xFF\xF2\x0A\x18\x00\x00\x00\x04'
ser.write(enia_mask_int)

# wmem 0xfff20a1c 0x00080000  
time.sleep(.500)
port_mask_int = b'\xC0\xFF\xF2\x0A\x1C\x00\x08\x00\x00'
ser.write(port_mask_int)

# Generate code  10 on interrupt, ack 
#wmem 0xfff20a24 0x00020019 
time.sleep(.500)
port_codegen_int = b'\xC0\xFF\xF2\x0A\x24\x00\x02\x00\x19'
ser.write(port_codegen_int)

#############################################################
# 2.7 Initialize the SIST
############################################################
# System Level test configuration 2
# wmem 0xffe00104 0x00000015
time.sleep(.500)
en_cfg2_sist = b'\xC0\xFF\xE0\x01\x04\x00\x00\x00\x10'
ser.write(en_cfg2_sist)

# Reset the Sist Port using SIST.PROT 
# wmem 0xffe0025c 0x55aa0040  
time.sleep(.500)
rst_prot_sist = b'\xC0\xFF\xE0\x02\x5C\x55\xAA\x00\x40'
ser.write(rst_prot_sist)

#  Enable Sist port
#wmem 0xffe0025c 0x55aa1f21  
time.sleep(.500)
en_prot_sist = b'\xC0\xFF\xE0\x02\x5C\x55\xAA\x1f\x21'
ser.write(en_prot_sist)


############################################################
# Start transmitting
############################################################
# System Level test configuration 2
# wmem 0xffe00104 0x00000015
time.sleep(.500)
en_cfg2_sist = b'\xC0\xFF\xE0\x01\x04\x00\x00\x00\x10'
ser.write(en_cfg2_sist)

# Reset Time counter
# wmem 0xffe00240 0x00000000  
time.sleep(.500)
rst_tim0_sist = b'\xC0\xFF\xE0\x02\x40\x00\x00\x00\x00'
ser.write(rst_tim0_sist)

# wmem 0xffe00244 0x00000000 
time.sleep(.500)
rst_tim1_sist = b'\xC0\xFF\xE0\x02\x44\x00\x00\x00\x00'
ser.write(rst_tim1_sist)

# Set Addr
#wmem 0xffe00200 0xfe131211  
time.sleep(.500)
set_addr1_sist = b'\xC0\xFF\xE0\x02\x00\xFE\x01\x00\x00'
ser.write(set_addr1_sist )

# Set packet length
#wmem 0xffe00228 0x00000001  
time.sleep(.500)
set_len_sist = b'\xC0\xFF\xE0\x02\x28\x00\x00\x00\x0F'
ser.write(set_len_sist )

# Set packet counter to 1.
#wmem 0xffe0023c 0x00010001  
time.sleep(.500)
count_pkt_sist = b'\xC0\xFF\xE0\x02\x3C\x00\x01\x00\x01'
ser.write(count_pkt_sist )

input("Press Enter to continue...")

#Packet Address size 0x1
#wmem 0xffe0022c 0xd3000001
#wmem 0xffe0022c 0xC1000001
time.sleep(.500)
en_txrx_sist = b'\xC0\xFF\xE0\x02\x2C\xC1\x00\x00\x01'
ser.write( en_txrx_sist )

time.sleep(2)

ser.close()

