from microbit import *
from ssd1309 import *
import music

display.off()
speaker.off()

pin6.set_pull(pin6.PULL_DOWN)
pin7.set_pull(pin7.PULL_DOWN)
pin8.set_pull(pin8.PULL_DOWN)
pin9.set_pull(pin9.PULL_DOWN)
pin10.set_pull(pin10.PULL_DOWN)

oled = SSD1309()
oled.clearScreen()

oled.textBlock((0, 0), "Hiya!")
oled.setPixel([100, 20], 1, False)
oled.setPixel([105, 20], 1, False)

oled.setPixel([100, 25], 1, False)
oled.setPixel([101, 26], 1, False)
oled.setPixel([102, 26], 1, False)
oled.setPixel([103, 26], 1, False)
oled.setPixel([104, 26], 1, False)
oled.setPixel([105, 25], 1, False)

oled.drawScreen()
sleep(1000)
spaceShip = sprites.sprite(sprites.spaceship)

spaceShipPosition = [0, 0]
oled.setSprite(spaceShip.sprite, spaceShipPosition)

while True:
    bit_0 = pin6.read_digital()
    bit_1 = pin7.read_digital()
    bit_2 = pin8.read_digital()
    bit_g = pin9.read_digital()
    bit_o = pin10.read_digital()

    packet = str(bit_o) + str(bit_g) + str(bit_2) + str(bit_1) + str(bit_0)
    oled.clearScreen()
    oled.textBlock((0, 0), packet)

    oled.drawScreen()

    #import speech

    #textBlock1 = "Greetings Profess or Falken. A strange game."
    #textBlock2 = "The only winning move, is not to play."
    #speech.say(textBlock1, speed=90, pitch=70, throat=150, mouth=150)
    #speech.say(textBlock2, speed=90, pitch=70, throat=150, mouth=150)

    #if packet == "011":
    #    spaceShipPosition = spaceShip.move("UP", spaceShipPosition, 1)
    #if packet == "001":
    #    spaceShipPosition = spaceShip.move("DOWN", spaceShipPosition, 1)
    #if packet == "010":
    #    spaceShipPosition = spaceShip.move("LEFT", spaceShipPosition, 1)
    #if packet == "000":
    #    spaceShipPosition = spaceShip.move("RIGHT", spaceShipPosition, 1)
    #if packet == "110":
    #    music.play(music.NYAN)

    #oled.setSprite(spaceShip.sprite, spaceShipPosition)
    #oled.drawScreen()
