

import pexpect
import sys
import chardet
import time


def bytestostr(bt):
    ret = chardet.detect(bt)
    return str(bt,encoding=ret['encoding'])
    

child = pexpect.spawn('adb shell ls /sys/class/gpio')
count = 0
value1 = []

start = time.time()
with open('tmpvalue3.txt','a+') as fo:
    fo.write("\n-----------------------\n")
    while True: 
        dirname = child.readline()
        if dirname:
            dirstr = bytestostr(dirname).strip()
            # print(dirstr)
            if dirstr.find('gpio') != -1 and dirstr.find('chip') == -1:
                print(dirstr[4:])
                cmd = 'adb shell cat /sys/class/gpio/{}/value'.format(dirstr)
                subchild = pexpect.spawn(cmd)
                strvalue = bytestostr(subchild.read()).strip()
                print(cmd,strvalue)
                if( strvalue == '1'):
                    fo.write(cmd+" "+strvalue +"\n")
                    value1.append(dirstr[4:])
                if subchild.isalive():
                    print("closeing")
                    subchild.close()
            count += 1

        else:

            break
    fo.write("\n")
    fo.write(str(value1)+'\n')

print('read count '+str(count)+" value1count "+str(len(value1)) + " time "+ str(time.time()-start))

# output = child.read()
# ret = chardet.detect(output)
# print(str(output,encoding=ret['encoding']))

# print(readline(child.logfile))