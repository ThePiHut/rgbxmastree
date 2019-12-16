from tree import RGBXmasTree
from colorzero import Color, Hue

tree = RGBXmasTree()

tree = Color('red')

while True:
    tree.color += Hue(deg=1)
