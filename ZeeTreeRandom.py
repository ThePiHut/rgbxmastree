from tree import RGBXmasTree
from colorzero import Color, Hue
import random
import time
from time import sleep

tree = RGBXmasTree()

tree.brightness = 0.1
timeout = 20

#starts Hue
def RGBXhue():
	timeout_start = time.time()
	tree.brightness = 0.1

	tree.color = Color('red')

	try:
		while time.time() < timeout_start + timeout:
			tree.color += Hue(deg=1)
	except KeyboardInterrupt:
                tree.brightness = 0.0
                tree.close()

#starts one by one
def OneByOne():
	timeout_start = time.time()
	tree.brightness = 0.1
	colors = [Color('red'), Color('green'), Color('blue')] # add more if you like

	try:
		while time.time() < timeout_start + timeout:
			for color in colors:
				for pixel in tree:
					pixel.color = color
	except KeyboardInterrupt:
                tree.brightness = 0.0
                tree.close()

#starts randomsparkles

def random_lights():
	timeout_start = time.time()
	tree.brightness = 0.1
	def random_color():
		r = random.random()
		g = random.random()
		b = random.random()
		return (r, g, b)

	try:
		while time.time() < timeout_start + timeout:
			pixel = random.choice(tree)
			pixel.color = random_color()
	except KeyboardInterrupt:
                tree.brightness = 0.0
                tree.close()

#starts rgb
def RuBeGe():
	timeout_start = time.time()
	tree.brightness = 0.1
	colors = [Color('red'), Color('green'), Color('blue')] # add more if you like

	try:
	    while time.time() < timeout_start + 10:
                    for color in colors:
                            tree.color = color
                            sleep(1)
	except KeyboardInterrupt:
                tree.brightness = 0.0
                tree.close()

try:
        my_list = [RGBXhue,OneByOne,random_lights,RuBeGe]
        while True:
                random.choice(my_list)()
##	while True:
##		print("RGBXhue")
##		RGBXhue()
##		print("1By1")
##		OneByOne()
##		print("random Sparks")
##		random_lights()
##		print("RBG")
##		RuBeGe()
except KeyboardInterrypt:
    tree.brightness = 0.0
    tree.close()

