with open("testgpio0.sh",'w+') as fo:
    fo.write("#!/bin/sh\n")
    for i in range(0,256):
        fo.write("echo "+str(i)+"\n")
        fo.write("echo "+str(i)+ " > /sys/class/gpio/export\n")
        print(i)

with open("testgpio288.sh",'w+') as fo:
    fo.write("#!/bin/sh\n")
    for i in range(288,288+24):
        fo.write("echo "+str(i)+"\n")
        fo.write("echo "+str(i)+ " > /sys/class/gpio/export\n")
        print(i)


with open("testgpio320.sh",'w+') as fo:
    fo.write("#!/bin/sh\n")
    for i in range(320,320+16):
        fo.write("echo "+str(i)+"\n")
        fo.write("echo "+str(i)+ " > /sys/class/gpio/export\n")
        print(i)


with open("testgpio336.sh",'w+') as fo:
    fo.write("#!/bin/sh\n")
    for i in range(336,336+24):
        fo.write("echo "+str(i)+"\n")
        fo.write("echo "+str(i)+ " > /sys/class/gpio/export\n")
        print(i)