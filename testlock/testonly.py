

import pexpect
import sys
import chardet
import time


def bytestostr(bt):
    ret = chardet.detect(bt)
    return str(bt,encoding=ret['encoding'])
    
numgpio = '327'

while True: 
    
    cmd = 'adb shell cat /sys/class/gpio/gpio{}/value'.format(numgpio)
    subchild = pexpect.spawn(cmd)
    strvalue = bytestostr(subchild.read()).strip()
    
    if( strvalue == '0'):
        print(cmd,strvalue)
        
        if subchild.isalive():
            print("closeing")
            subchild.close()
    else:
        print(strvalue)