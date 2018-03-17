from machine import I2C, Pin
i2c = I2C(scl=Pin(5), sda=Pin(4))

print(i2c.scan())

from ssd1306 import *
oled = SSD1306_I2C(128,64,i2c)
oled.text("ahoj",1,1,1)
oled.show()
