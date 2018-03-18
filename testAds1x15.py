import ads1x15
from machine import I2C, Pin
i2c = I2C(scl=Pin(5), sda=Pin(4))

ads = ads1x15.ADS1015(i2c=i2c)

while True:
    print(ads.read(0),ads.read(1))
