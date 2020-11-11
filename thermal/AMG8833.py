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

        def __init__(self, bus):
                self.bus = bus
                self.i2c_address = 0x68
                self.__coefData2Tem = 2.5

                self.__setup()


        def __setup(self):
            pass
