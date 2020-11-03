# Dependencies
`smbus2`
https://github.com/kplindegaard/smbus2

```bash
$ pip3 install -r requirements.txt
```

# Usage
```python3
bus = SMBus(busNumber)
data = BME280(bus).readData() # format: tuple(float(temperature), float(pressure), float(humidity))
```
## check busNumber
```bash
# i2cdetect -l
```