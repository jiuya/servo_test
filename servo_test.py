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
    def __del__(self):
        self.h2pLwServoAddr.close()
        os.close(self.fd)
    def write_data(self,wordData):
        self.h2pLwServoAddr.write_byte(chr(wordData))
    def write_word(self,addr,word):
        self.set_pos(addr)
        self.write_data(word & 0xff)
        self.write_data((word >> 8) & 0xff)
    def set_pos(self,pos):
        self.h2pLwServoAddr.seek(pos,os.SEEK_SET)
    def read_data(self):
        return self.h2pLwServoAddr.read_byte()
    def set_period(self,num,period):
        if num > 4:
            return
        self.write_word(num*2,period)
    def set_compare(self,num,cmp):
        if num > 4:
            return
        self.write_word(num*2+8,cmp)
    def set_divider(self,div):
        self.write_word(16,div)
    def init(self,num):
        self.set_divider(4)
        self.set_period(num,62500)
        self.set_compare(num,3125)
    def angle(self,num,angle):
        self.set_compare(num,57870*angle+2187.5)

if __name__ == '__main__':
    servo = Servo()

    #servo.set_divider(0)
    servo.set_period(0,0xff)
    servo.set_compare(0,0x7f)
    """
    for var in range(0,20):
        servo.h2pLwServoAddr.write_byte(chr(0))
    """
