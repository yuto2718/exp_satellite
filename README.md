# exp_satellite
<img src="https://img.shields.io/badge/LICENSE-MIT-green">
<img src="https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat">

特別実験 後期Aコースにて製作したプログラム．

配布された各センサの情報の取得，Monostickを用いた通信用のモジュールである．

2020/11/30以降の保守管理はしていないため，動作は保障しない．

# Dependencies
`micropyGPS`
https://github.com/inmcm/micropyGPS

`smbus2`
https://github.com/kplindegaard/smbus2

`pySerial`
https://github.com/pyserial/pyserial

# センサ
- `GPS` https://akizukidenshi.com/catalog/g/gK-09991/
- `温湿度，気圧 `
- `9軸(加速度，角速度，地磁気)` https://strawberry-linux.com/catalog/items?code=12250
- `8*8ピクセルサーモセンサ` https://www.switch-science.com/catalog/3395/

# 通信
- `Monostick`
https://mono-wireless.com/jp/products/MoNoStick/index.html
