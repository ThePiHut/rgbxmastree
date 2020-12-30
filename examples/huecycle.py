#!/usr/bin/env python3

from tree import RGBXmasTree
from colorzero import Color, Hue

tree = RGBXmasTree()

tree.color = Color('red')

try:
    while True:
        tree.color += Hue(deg=1)
except KeyboardInterrupt:
    tree.off()
    tree.close()
