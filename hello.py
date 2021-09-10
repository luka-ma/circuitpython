import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("make it red!")
dot.brightness = 0.2
while True:
    dot.fill((255, 0, 0))