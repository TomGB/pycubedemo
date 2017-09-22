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
        self.startStrength = 8

        return 1.0/10

    def trySetPixel(self, pos, colour):
        if pos[0] >= 0 and pos[0] < 8 and pos[1] >= 0 and pos[1] < 8 and pos[2] >= 0 and pos[2] < self.startStrength :
            self.cube.set_pixel(pos, colour)
    def tick(self):
        self.cube.clear()

        newItem = type('obj', (object,), { 'pos': (random.randint(0, 8), random.randint(0, 8), 7), 'speed': 10, 'strength': self.startStrength })

        self.items.append(newItem)

        for item in self.items:
            self.trySetPixel(item.pos, (0, 255 * item.strength / self.startStrength, 0))

        for item in reversed(self.items):
            if item.strength > 0:
                item.pos = (item.pos[0], item.pos[1], item.pos[2] - 1)
            if item.strength > 0 and item.pos[2] == 6:
                newItem = type('obj', (object,), { 'pos': (item.pos[0], item.pos[1], item.pos[2] + 1), 'speed': item.speed, 'strength': item.strength - 1 })
                self.items.append(newItem)
            if item.pos[2] < 0 or item.strength <= 0:
                self.items.remove(item)
