from lib import *
from math import pi, acos, atan2

class Envmap(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        img = open(self.path, "rb")
        img.seek(10)
        headerSize = struct.unpack('=l', img.read(4))[0]

        img.seek(14 + 4)
        self.width = struct.unpack('=l', img.read(4))[0]
        self.height = struct.unpack('=l', img.read(4))[0]

        img.seek(headerSize)
        self.pixels = []
        for y in range(self.height):
            for x in range(self.width):
                b = ord(img.read(1)) 
                g = ord(img.read(1)) 
                r = ord(img.read(1)) 

                self.pixels.append(b)
                self.pixels.append(g)
                self.pixels.append(r)

        img.close()

    def get_color(self, direction, intensity=1):
      width = 2000
      height = 1000
      direction = norm(direction)

      x = int((atan2(direction.z, direction.x) / (2 * pi) + 0.5) * width)
      y = int(acos(-direction.y) / pi * height)
      index = (y * self.width + x) * 3 % len(self.pixels)

      processed = self.pixels[index:index+3] * intensity
      return color(processed[2], processed[1], processed[0])