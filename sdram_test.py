import os
import sys
import mmap

class Servo:
    hwRegsSpan = 0x200000
    hwRegsBase = 0xff200000
    def __init__(self):
        self.fd = os.open("/dev/mem",os.O_RDWR | os.O_SYNC)
        self.h2pLwServoAddr = mmap.mmap(self.fd, Servo.hwRegsSpan,
                mmap.MAP_SHARED,mmap.PROT_READ | mmap.PROT_WRITE,
                offset=Servo.hwRegsBase)
        self.h2pLwServoAddr.seek(0x100000,os.SEEK_SET)
    def __del__(self):
        self.h2pLwServoAddr.close()
        os.close(self.fd)
    def writeData(self,wordData):
        self.h2pLwServoAddr.write_byte(chr(wordData))
    def posReset(self,pos):
        self.h2pLwServoAddr.seek(0x100000+pos,os.SEEK_SET)
    def readData(self):
        return self.h2pLwServoAddr.read_byte()

if __name__ == '__main__':
    servo = Servo()
    servo.posReset(1)
    for var in range(0,20):
        servo.writeData(var*2)
        print '%4d' % var ,
    print ""
    servo.posReset(0)
    servo.writeData(1)
    while servo.readData() == 1:
        servo.posReset(0)
    servo.posReset(21)
    for var in range(0,20):
        print  '%4d' % ord(servo.readData()) ,
    print ""
