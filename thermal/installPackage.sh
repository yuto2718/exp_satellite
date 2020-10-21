echo "installing SMBus2 package\n"
pip3 install smbus2 > /dev/null && echo "i2c address: ";sudo i2cdetect -y 1
