#!/usr/bin/env python3
# coding: utf-8

# MPU9248: Slave Address - 0b1101000(gyro,accel.) & 0b1100(compass)

def __word_swap(data):
    ret = data << 8
    ret = ret | (data >> 8)
    return 0xFFFF & ret

#def __word_swap(data):
#    return (data & 0xFF00 >> 8) | (data & 0x00FF << 8)


class MPU9250:
    # bus: SMBus instance
    def __init__(self, bus):
        self.bus = bus
        self.GYRO_ADDR = 0b1101001   # AD0: H
        self.ACCEL_ADDR = 0b1101001  # AD0: H
        self.COMPASS_ADDR = 0b1100

        self.GYRO_OFFSET = 0x3B
        self.ACCEL_OFFSET = 0x3B + 0x06
        self.COMPASS_OFFSET = 0x03
        self.__setup()

    def getGyro(self):
        x = self.__readWord(self.GYRO_ADDR, self.GYRO_OFFSET)
        y = self.__readWord(self.GYRO_ADDR, self.GYRO_OFFSET + 0x02)
        z = self.__readWord(self.GYRO_ADDR, self.GYRO_OFFSET + 0x04)
        return (x, y, z)

    def getAccel(self):
        x = self.__readWord(self.ACCEL_ADDR, self.ACCEL_OFFSET)
        y = self.__readWord(self.ACCEL_ADDR, self.ACCEL_OFFSET + 0x02)
        z = self.__readWord(self.ACCEL_ADDR, self.ACCEL_OFFSET + 0x04)
        return (x, y, z)

    def getCompass(self):
        x = self.__word_swap(self.__readWord(self.COMPASS_ADDR, self.COMPASS_OFFSET))
        y = self.__word_swap(self.__readWord(self.COMPASS_ADDR, self.COMPASS_OFFSET + 0x02))
        z = self.__word_swap(self.__readWord(self.COMPASS_ADDR, self.COMPASS_OFFSET + 0x04))
        return (x, y, z)

    def __writeReg(self, i2c_address, reg_address, data):
        self.bus.write_byte_data(i2c_address, reg_address, data)

    def __readWord(self, i2c_addr, reg_addr):
        msB = self.bus.read_byte_data(i2c_addr, reg_addr)
        lsB = self.bus.read_byte_data(i2c_addr, reg_addr + 1)
        return (msB << 8) | lsB

    def __setup(self):
        self.__writeReg(self.GYRO_ADDR, 0x6b, 0x00)
        self.__writeReg(self.GYRO_ADDR, 0x37, 0x02)
        self.__writeReg(self.COMPASS_ADDR, 0x0A, 0x12)
