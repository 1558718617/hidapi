import pywinusb.hid.core as hidCore

import random
from time import sleep


hidDevs = hidCore.find_all_hid_devices()
for hiddev in hidDevs:
    if hiddev.product_id == 0x5750 and hiddev.vendor_id == 0x0483:
        myHid = hiddev
        break

print(myHid)
#if not myHid.is_opened:
myHid.open()

outReport = myHid.find_output_reports()[0]
inReport = myHid.find_input_reports()[0]

print('out report',outReport)

print('in report',inReport)

#print(outReport._HidReport__usage_data_list)

txBuf = [i for i in range(17)]
rxBuf = [0 for i in range(17)]

#outReport.set_raw_data(txBuf)
#inReport.set_raw_data(rxBuf)

for i in range(17):
    txBuf[i] = i
    

while True:
    for i in range(1,17):
        txBuf[i] = random.randint(0,255)
    print('Send: ',txBuf)
    myHid.send_output_report(txBuf)
    
    rxBuf = myHid.get_input_report()
    if rxBuf != None:
        print('Read : ',rxBuf)
    sleep(1)
    
myHid.close()




