import sys
import logging

import board
import neopixel


class StatusLED(object):

    def __init__(self, software_only):
        self.software_only = software_only
        if self.software_only: return

        self.pixels = neopixel.NeoPixel(board.D18, 1)

    def swap_blue_green(self):
        pass

    def set_color(self, red, green, blue):
        if self.software_only: return

        self.pixels[0] = (red * 255, green * 255, blue * 255)
