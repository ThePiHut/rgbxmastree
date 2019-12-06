from tree import RGBXmasTree
from colorzero import Hue

tree = RGBXmasTree()

tree = Color('red')

while True:
    tree.color += Hue(deg=1)
