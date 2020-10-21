#! /usr/bin/env python3
#coding: utf-8

# from smbus2 import SMBus

def __word_swap(data):
    return (data & 0xFF00 >> 8) | (data & 0x00FF << 8)

class MPU9250:
    def __init__(self, bus):
        self.bus = bus # SMBus instance
        self.GYRO_ADDR = 0b1101000 # AD0: L
        self.ACCEL_ADDR = 0b1101000
        self.COMPASS_ADDR = 0b1100

        self.GYRO_OFFSET = 0x3B
        self.ACCEL_OFFSET = 0x3B + 0x06
        self.COMPASS_OFFSET = 0x03
        
    def getGyro():
        x = __readWord(GYRO_ADDR, GYRO_OFFSET)
        y = __readWord(GYRO_ADDR, GYRO_OFFSET + 0x02)
        z = __readWord(GYRO_ADDR, GYRO_OFFSET + 0x04)
        return (x, y, z)

    def getAccel():
        x = __readWord(ACCEL_ADDR, ACCEL_OFFSET)
        y = __readWord(ACCEL_ADDR, ACCEL_OFFSET + 0x02)
        z = __readWord(ACCEL_ADDR, ACCEL_OFFSET + 0x04)
        return (x, y, z)

    def getCompass():
        x = __word_swap(__readWord(COMPASS_ADDR, COMPASS_OFFSET))
        y = __word_swap(__readWord(COMPASS_ADDR, COMPASS_OFFSET + 0x02))
        z = __word_swap(__readWord(COMPASS_ADDR, COMPASS_OFFSET + 0x04))        
        return (x, y, z)

    def __writeReg(i2c_address, reg_address, data):
        bus.write_byte_date(i2c_address, reg_address, data)

    def __readWord(i2c_addr, reg_addr):
        msB = bus.read_byte_data(i2c_addr,reg_addr)
        lsB = bus.read_byte_data(i2c_addr,reg_addr+1)
        return (msB << 8) | lsB

    def __setup():
        # setup 
        __writeReg(GYRO_ADDR,0x6b,0x00)
        __writeReg(GYRO_ADDR,0x37,0x02)
        __writeReg(COMPASS_ADDR,0x0A,0x12)
