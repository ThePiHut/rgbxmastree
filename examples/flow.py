import argparse
from time import sleep
from tree import RGBXmasTree
from colorzero import Color


tree = RGBXmasTree(auto_update=False)

# create lists of tree pixel offsets for each row
bottom_row = [0, 6, 19, 24, 6, 12, 15, 16, 7]
middle_row = [1, 5, 20, 23, 5, 11, 14, 17, 8]
top_row = [2, 4, 21, 22, 4, 10, 13, 18, 9]
star = [3]

# list of rows in order from bottom to top
order = [bottom_row, middle_row, top_row, star]

# provide CLI parametes
parser = argparse.ArgumentParser(
    description="Colours flow up the RGB Xmas tree "
    "https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi"
    " https://github.com/gilesknap/raspitree"
)
parser.add_argument(
    "--brightness", help="brightness for all LEDs", type=float, default=0.1
)
parser.add_argument(
    "--degrees", help="hue separation between each row", type=int, default=80
)
parser.add_argument("--pause", help="pause after update in secs", type=float, default=0)
args = parser.parse_args()

tree.brightness = args.brightness
tree.on()

hue = 0

while True:
    for row in order:
        hue += args.degrees / 360
        hue %= 1.0
        for pixel_number in row:
            c = Color.from_hsv(hue, 1.0, 1.0)
            tree[pixel_number].color = c
    tree.update()
    sleep(args.pause)
