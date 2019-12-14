from tree import RGBXmasTree
from colorzero import Color

tree = RGBXmasTree()

colors = [Color('red'), Color('green'), Color('blue')] # add more if you like

while True:
    for color in colors:
        for pixel in tree:
            pixel.color = color
