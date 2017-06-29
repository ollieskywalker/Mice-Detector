import threading
from threading import Thread
import reader1


reader1 = reader.Reader(0x16c0, 0x27db, 36, 3, should_reset=False)
reader2 = reader.Reader(0x16c0, 0x27db, 36, 3, should_reset=False)

device = list(usb.core.find(find_all=True, idVendor=0x16c0, idProduct = 0x27db))

reader1.initialize(device[0])
reader2.initialize(device[1])

file = open("RFID_log1.txt", "w")

#reader2.initialize()
while True:
	file.write(str(reader1.read()))
	
reader1.disconnect()
file.close()