from tree import RGBXmasTree
from colorzero import Hue, Color

tree = RGBXmasTree()

tree.color = Color('red')

while True:
    tree.color += Hue(deg=1)
