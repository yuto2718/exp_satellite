# Dependencies
`micropyGPS`
https://github.com/inmcm/micropyGPS

```bash
$ pip3 install -r requirements.txt
```

# Usage
```python3
serial = serial.Serial('#serial port device file#', 9600, timeout=5)
my_gps = GYSFDMAXB(serial)
my_gps.getLatitude()
del gps # release Serial Port
```
