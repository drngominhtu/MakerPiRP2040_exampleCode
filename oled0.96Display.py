from machine import Pin, I2C
from sh1106 import SH1106_I2C
import time

# Khởi tạo I2C trên GP2 (SDA), GP3 (SCL)
i2c = I2C(1, scl=Pin(14), sda=Pin(15), freq=400000)

# Tạo đối tượng OLED 1.3 inch (128x64)
oled = SH1106_I2C(128, 64, i2c)

# Hiển thị nội dung
oled.fill(0)
oled.text("Hello Maker Pi!", 0, 0)
oled.text("OLED 1.3 SH1106", 0, 10)
oled.show()
