class AMG8833:
        # usage: hoge = BME($SMBus)
        PCTL = 0x00
        RST  = 0x01
        FPSC = 0x02
        INTC = 0x03
        STAT = 0x04
        SCLR = 0x05
        AVE  = 0x07
        INTHL= 0x08
        TTHL = 0x0E
        INT0 = 0x10
        T01L = 0x80
        TRS  = 0x80

        def __init__(self, bus):
                self.bus = bus
                self.i2c_address = 0x68
                self.__coefData2Tem = 2.5

                self.__setup()


        def __setup(self):
            self.__writeReg(AMG8833.FPSC, 0xA)

        def __writeReg(self,reg_address, data):
            self.bus.write_byte_data(self.i2c_address,reg_address,data)

        def getPixelTemperature(self, pixelAddr):
            pixelLowRegister = AMG8833.TRS + (2 * pixelAddr);
            tempLow = self.bus.read_byte_data(self.i2c_address,pixelLowRegister)
            tempHigh = self.bus.read_byte_data(self.i2c_address,pixelLowRegister+1)
            temperature = tempLow + tempHigh*0xFF
            # temperature is reported as 12-bit twos complement
            # check if temperature is negative
            if(temperature & (1 << 11)):
                temperature &= ~(1 << 11);
                temperature = temperature * -1;
            DegreesC = temperature*0.25
            return DegreesC;
