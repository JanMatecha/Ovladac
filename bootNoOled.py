from machine import I2C, Pin
from ssd1306 import *

i2c = I2C(scl=Pin(5), sda=Pin(4))

#oled = SSD1306_I2C(128,64,i2c)

print("start boot.py")
#oled.text("start boot.py",1,1,1)
#oled.show()

import myNetwork
text = myNetwork.do_connect()

#oled.text(text[1][0],1,10,1)
#oled.show()



import webrepl
#oled.text("import webrepl",1,20,1)
#oled.show()
webrepl.start()
#oled.text("webrepl.start()",1,30,1)
#oled.show()

import gc
gc.collect()

print("konec boot.py")
#oled.text("konec boot.py",1,50,1)
#oled.show()

