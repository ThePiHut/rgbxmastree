from tree import RGBXmasTree

tree = RGBXmasTree()

colors = [Color('red'), Color('green'), Color('blue')] # add more if you like

while True:
    for color in colors:
        tree.color = color
