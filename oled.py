from machine import I2C, Pin
from ssd1306 import *
from myNetwork import *


class Oled(SSD1306_I2C):

    def __init__(self):
        self.i2c = I2C(scl=Pin(5), sda=Pin(4))
        self._width = 128
        self._height = 64
        self._head_width = self._width
        self._head_height = 10
        self._foot_width = self._width
        self._foot_height = 10


        super().__init__(128, 64, self.i2c)
        pass

    def head(self, width=None, height=None, ip=None):

        if ip is None:
            ip = get_ip()

        if width is not None:
            self.head_width = width
        if height is not None:
            self.head_height = height

        self.fill_rect(0, 0, self.head_width, self.head_height, 0)
        self.text(ip, 0, 0)
        self.show()

    def square(self, x1=None, y1=None, x2=None, y2=None):
        #TODO dodelat promenne pro ctverec

        self.fill_rect(43, 11, 40, 40, 0)
        self.rect(43, 11, 40, 40, 1)
        self.show()

    def show_position(self, x=None, y=None):
        self.fill_rect(44, 12, 38, 38, 0)
        self.pixel(x, y, 1)
        self.line(x - 2, y, x + 2, y, 1)
        self.line(x, y - 2, x, y + 2, 1)
        self.show()
        pass

    def foot(self, width=None, height=None, ip=None):

        if ip is None:
            ip = get_ip()

        if width is not None:
            self.head_width = width
        if height is not None:
            self.head_height = height

        self.fill_rect(0, 53, self.head_width, self.head_height, 0)
        self.text(ip, 0, 55)
        self.show()

    @property
    def head_width(self):
        return self._head_width

    @head_width.setter
    def head_width(self, value):
        self._head_width = value

    @property
    def head_height(self):
        return self._head_height

    @head_height.setter
    def head_height(self, value):
        self._head_height = value


    @property
    def foot_width(self):
        return self._foot_width

    @foot_width.setter
    def foot_width(self, value):
        self._foot_width = value

    @property
    def foot_height(self):
        return self._foot_height

    @foot_height.setter
    def foot_height(self, value):
        self._foot_height = value


    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


def main():
    print("main")
    oled = Oled()
    oled.text("ahoj", 1, 1, 1)
    oled.show()


if __name__ == "__main__":
    # execute only if run as a script
    main()


