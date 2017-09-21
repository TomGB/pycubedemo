# wave
# Copyright (C) Paul Brook <paul@nowt.org>
# Released under the terms of the GNU General Public License version 3

import random
import cubehelper
import math

class Pattern(object):
    def init(self):
        self.double_buffer = True

        self.step = 0

        return 1.0/10

    def trySetPixel(self, pos, colour):
        if pos[0] >= 0 and pos[0] < 8 and pos[1] >= 0 and pos[1] < 8 and pos[2] >= 0 and pos[2] < 8 :
            self.cube.set_pixel(pos, colour)
    def tick(self):
        self.cube.clear()

        self.step += 1
        self.step %= 3

        mainColor = (255, 255, 255)
        secondColor = (200, 200, 200)
        thirdColor = (100, 100, 100)

        print(self.step)

        for x in range(3):
            for y in range(8):
                for z in range(2):
                    self.trySetPixel((self.step + x*3, y, z*7), mainColor)
                    self.trySetPixel((self.step + x*3 - 1, y, z*7), secondColor)
                    self.trySetPixel((self.step + x*3 - 2, y, z*7), thirdColor)
            for y in range(2):
                for z in range(8):
                    self.trySetPixel((self.step + x*3, y*7, z), mainColor)
                    self.trySetPixel((self.step + x*3 - 1, y*7, z), secondColor)
                    self.trySetPixel((self.step + x*3 - 2, y*7, z), thirdColor)

        for x in range(3):
            for y in range(6):
                for z in range(2):
                    self.trySetPixel((2 - self.step + x*3, 1+y, 1+z*5), mainColor)
                    self.trySetPixel((2 - self.step + x*3 - 1, 1+y, 1+z*5), secondColor)
                    self.trySetPixel((2 - self.step + x*3 - 2, 1+y, 1+z*5), thirdColor)
            for y in range(2):
                for z in range(6):
                    self.trySetPixel((2 - self.step + x*3, 1+y*5, 1+z), mainColor)
                    self.trySetPixel((2 - self.step + x*3 - 1, 1+y*5, 1+z), secondColor)
                    self.trySetPixel((2 - self.step + x*3 - 2, 1+y*5, 1+z), thirdColor)
