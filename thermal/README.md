# Dependencies
`smbus2`
https://github.com/kplindegaard/smbus2

```bash
$ pip3 install -r requirements.txt
```

# Usage
```python3
bus = SMBus(busNumber)
BME280(bus).readData()
```