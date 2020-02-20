# pyGRMON
Usage of the UART master of the GR718B

## UART Interface

The protocol allows a read or write transfer to be generated to any address on the AMBA AHB bus

## Transmission protocol

The interface supports a simple protocol where commands consist of a control byte, followed by a 32-bit address, followed by optional write data.


### READ command
	We have to transmit a read command, the header is:
	|Byte | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | Description |
	|    0 | 1 | 0 | L5 | L4 | L3 | L2 | L1 | L0 | 10 -> Denotes Command Read; L[5..0] Is the number of words to read: Length-1 |
	|    1 | Addr 31 | Addr 30 | Addr 29 | Addr 28 | Addr 27 | Addr 26 | Addr 25 | Addr 24 | Addr 31..24 |  
	|    2 | Addr 23 | Addr 22 | Addr 21 | Addr 20 | Addr 19 | Addr 18 | Addr 17 | Addr 16 | Addr 23..16 |
	|    3 | Addr 15 | Addr 14 | Addr 13 | Addr 12 | Addr 11 | Addr 10 | Addr 09 | Addr 08 | Addr 15..8 |
	|    4 | Addr 07 | Addr 06| Addr 05 | Addr 04 | Addr 03 | Addr 02 | Addr 1 | Addr 00 | Addr 7..0 |


- Read Example:
	Read Version / instance ID regiser (RTR.VER) AMBA Addr: 0xFFF20A08  RMAP Addr: 0x00000A08  	
	| Byte | Value | Description		|  
	| 0 | 80	| Read Command. Read Lenth = 1 Word.|
	| 1 | FF	| AMBA ADDR = 0xFFF20A08 |  
	| 2 | F2	|  |  
	| 3 | 0A	|  |  
	| 4 | 08	|  |  
	| Command | 0x80 0xFF 0xF2 0x0A 0x08


Expected Result: 0x01 0x03 0x 00 0x00

	| 31 24| 23 16| 15 8| 7 4| 3 0 | 
	|  MA  |  MI   | PA |   ID     |
	| 0x01 | 0x03  |  0x00| 0x0 | *| 

	31: 24 Major version (MA) - Holds the major version number of the router. Constant value 0x01.
	23: 16 Minor version (MI) - Holds the minor version number of the router. Constant value 0x03.
	15: 8 Patch (PA) - Holds the patch number of the router. Constant value 0x00.
	7: 0 Instance ID (ID) - Holds the instance ID number of the router. Reset value for bits 3:0 is set through GPIO[23:0] pins, as specified in section 5.


### Write command
	Write Spw2 ctrl  (RTR.PCTRL) AMBA Addr: 0xFFF20808  RMAP Addr: 0x00000A08 Value: 0x081404F0
	|Byte | Value | Description		|
	| 0 | C0	| Write Command. Write Lenth = 1 Word.|
	| 1 | FF	| AMBA ADDR = 0xFFF20A08 |
	| 2 | F2	|  |
	| 3 | 0A	|  |
	| 4 | 08	|  |
	| 5 | 08	|  |
	| 6 | 14	| |
	| 7 | 04	| |
	| 8 | F0	| |
	| Command | 0xC0 0xFF 0xF2 0x0A 0x08 0x08 0x14 0x04 0xF0


## Install
Requires Python3, pySerial.
```
$]# sudo python3 -m pip install pyserial
```
