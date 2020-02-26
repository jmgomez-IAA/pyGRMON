# 1.1 SW reset the complete router via RTR.RTRCFG.RE bit
wmem 0xfff20a00 0x9002c183 
  
# # 2.0  Clearing Spw 1 port counters
# wmem 0xfff20c10 0xffffffff  
# wmem 0xfff20c14 0xffffffff  
# wmem 0xfff20c18 0xffffffff  
# wmem 0xfff20c1c 0xffffffff  

# # 2.1  Clearing SIST port counters
# wmem 0xfff20d30 0xffffffff  
# wmem 0xfff20d34 0xffffffff  
# wmem 0xfff20d38 0xffffffff  
# wmem 0xfff20d3c 0xffffffff 

# # 2.2 Clearing RTR.PSTS1 error bits
# wmem 0xfff20884 0x0000a01f    

# # 2.3 Clearing all SIST.ERROR registers
# wmem 0xffe00230 0x00000000  
# wmem 0xffe00234 0x00000000  
# wmem 0xffe00238 0x00000000  
  
# 2.4 Enable ports Spw1
# Repetido lo hab en paso 1.2
wmem 0xfff20804 0x0010002e  
#Enable SIST en PCTL y PCTRL2
wmem 0xfff2084c 0x00008020  
wmem 0xfff209cc 0xc000de00  

# 2.7 Systest configuration (Enable SIST.PORT)
wmem 0xffe00104 0x00000010

# 2.8 SW reset the SIST via SIST.PROT.RST bit
wmem 0xffe0025c 0x55aa0040  

# 2.9  Enable sist port after reset, SIST.PROT.RST bit = 1.
wmem 0xffe0025c 0x55aa0001
# Enable with global interupts.
#wmem 0xffe0025c 0x55aa1f21

# 3.0 Disable all internal loop-backs by configuring SYSTEST.CFG1 & SYSTEST.CFG2 
wmem 0xffe00100 0x00000000  
wmem 0xffe00104 0x00000010

# 4.0 Create the packet.
wmem 0xffe00240 0x00000000  
wmem 0xffe00244 0x00000000  
wmem 0xffe00200 0xfe010000  
wmem 0xffe00214 0x00000000  
wmem 0xffe00218 0x00000000  
wmem 0xffe0021c 0x00000000  
wmem 0xffe00228 0x000000FF  
wmem 0xffe0023c 0x00010001 

# 4.1 Run Tx Test
wmem 0xffe0022c 0x81000001

# Transmit packet indefinetly
#wmem 0xffe0022c 0xE1000001
