# wave
# Copyright (C) Paul Brook <paul@nowt.org>
# Released under the terms of the GNU General Public License version 3

import random
import cubehelper
import math

class Pattern(object):
    def init(self):
        self.double_buffer = True

        self.items = []

        return 1.0/10

    def trySetPixel(self, pos, colour):
        if pos[0] >= 0 and pos[0] < 8 and pos[1] >= 0 and pos[1] < 8 and pos[2] >= 0 and pos[2] < 8 :
            self.cube.set_pixel(pos, colour)
    def tick(self):
        self.cube.clear()

        newItem = type('obj', (object,), { 'pos': (random.randint(0, 8), random.randint(0, 8), 7), 'speed': 10, 'strength': 8 })

        self.items.append(newItem)

        mainColor = (0, 255, 0)
        secondColor = (200, 200, 200)
        thirdColor = (100, 100, 100)

        for item in self.items:
            self.trySetPixel(item.pos, mainColor)

        for item in self.items:
            if item.strength > 0 :
                item.pos = (item.pos[0], item.pos[1], item.pos[2] - 1)
                newItem = type('obj', (object,), { 'pos': (item.pos[0], item.pos[1], item.pos[2] + 1), 'speed': item.speed, 'strength': item.strength - 1 })
            if item.pos[2] <0 :
                items.remove(item)
