# SPI Code developed for the DIYMore SPI/IIC Screen
from microbit import *
# from microbit import spi, pin16, pin14, pin15, Image

class SSD1309():
    def __cmd(self, c):
        pin16.write_digital(0)
        spi.write(bytearray(c))
        pin16.write_digital(1)

    def __init__(self):
        c = b'\xAE\xA4\xD5\xF0\xA8\x3F\xD3\x00\x00\x8D'  \
            b'\x14\x20\x00\x21\x00\x7F\x22\x00\x3F\xa1'  \
            b'\xc8\xDA\x12\x81\xCF\xd9\xF1\xDB\x40\xA6\xd6\x00\xaf'
        pin14.write_digital(0)
        spi.init(miso=pin15,
                 baudrate=8000000)
        pin14.write_digital(1)

        self.__cmd(c)
        self.screen = bytearray(1024)

    def __set_pos(self, col=0, page=0):
        c1, c2 = col * 2 & 0x0F, col >> 3
        self.__cmd([0xb0 | page, 0x00 | c1, 0x10 | c2])

    def clearScreen(self):
        for i in range(0, 1024):
            self.screen[i] = 0
        self.drawScreen()

    def drawScreen(self):
        self.__set_pos()
        spi.write(self.screen)

    def setPixel(self, coOrdinates: tuple, color: int):
        page, shiftPage = divmod(coOrdinates[1], 8)
        i = coOrdinates[0] + page * 128 + 1
        bites = self.screen[i] | (1 << shiftPage) if color else self.screen[
                i] & ~ (1 << shiftPage)
        self.screen[i] = bites
        self.__set_pos(coOrdinates[0], page)
        spi.write(bytearray([bites]))

    def getPixel(self, coOrdinates: tuple):
        page, shiftPage = divmod(coOrdinates[1], 8)
        i = coOrdinates[0] + page * 128 + 1

        return (self.screen[i] & (1 << shiftPage)) >> shiftPage

    def textBlock(self, coOrdinates: tuple, text, size: int = 1):
        for i in range(0, min(len(text), 25//size - coOrdinates[0])):
            for column in range(0, 5):
                col = 0
                for row in range(1, 6):
                    pixel = Image(text[i]).get_pixel(column, row - 1)
                    col = col | (1 << row * size) if (pixel != 0) else col
                ind = ((coOrdinates[0] * 5 * size) + (coOrdinates[1] * 128) +
                       (i * 5 * size) + (column * size) + 1)
                if size == 2:
                    self.screen[ind + 128], self.screen[ind] = divmod(col, 0x100)
                    self.screen[ind + 1] = self.screen[ind]
                    self.screen[ind + 129] = self.screen[ind + 128]
                else:
                    self.screen[ind] = col
        self.drawScreen()

if __name__ == "__main__":
    # Test the Module
    oled = SSD1309()
    oled.clearScreen()
    oled.textBlock((0, 0), "Hiya!")
    oled.setPixel((126, 63), 1)
    oled.drawScreen()
