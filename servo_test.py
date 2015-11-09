import mmap

class Servo:
    def __init__(self):
        hwRegsSpan = 0x200000
        hwRegsBase = 0xff200000
        h2pLwServoAddr = None
    def open(self):
        fd = open("/dev/mem","r+b")
        h2pLwServoAddr = mmap.mmap(fd.fileno(), hwRegsSpan,MAP_SHARED, ( PROT_READ | PROT_WRITE ),hwRegsBase)
        h2pLwServoAddr = virtual_base + 0x100000
        h2pLwServoAddr.seek(0x100000,os.SEEK_SET)
    def writeData(self,wordData):
        write_byte(wordData)
    def posReset(self):
        h2pLwServoAddr.seek(0x100000,os.SEEK_SET)
    def readData(self):
        return read_byte()

if __name__ == '__main__':
    servo = Servo();
    for var in range(0,10):
        servo.writeData(var)
        print var + " "
    print "\n"
    servo.posReset()
    for var in range(0,10):
        print servo.readData() + " "
    print "\n"
