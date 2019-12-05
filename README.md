# rgbxmastree

Code examples for the RGB Xmas Tree

## Getting started

Start by downloading the xmas tree file. Open a terminal and type:

```bash
wget http://goo.gl/rgbxmastree -O tree.py
```

When you write your own Python code, make sure you keep this file in the same
folder.

Open a Python shell or IDE (like Mu, Thonny or IDLE) and import `RGBXmasTree`:

```python
from tree import RGBXmasTree
```

Initialise your tree:

```python
from tree import RGBXmasTree

tree = RGBXmasTree()
```

## Change the brightness

You can change the brightness from 0 to 1 - the default is 0.5:

```python
from tree import RGBXmasTree

tree = RGBXmasTree(brightness=0.1)
```

You'll find that 1 is _extremely bright_ and even 0.1 is plenty bright enough if
the tree is on your desk :)

## Change the colour

You can set the colour of all the LEDs together using RGB values (all 0-1):

```python
from tree import RGBXmasTree

tree = RGBXmasTree()

tree.color = (1, 0, 0)
```

Alternatively you can use the `colorzero` library:

```python
from tree import RGBXmasTree
from colorzero import Color

tree = RGBXmasTree()

tree.color = Color('red')
```

You can write a loop to repeatedly cycle through red, green and blue:

```python
from tree import RGBXmasTree
from time import sleep

tree = RGBXmasTree()

colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

for color in colors:
    tree.color = color
    sleep(1)
```

## Individual control

You can also control each LED individually, for example turn each one red, one
at a time:

```python
from tree import RGBXmasTree
from time import sleep

tree = RGBXmasTree()

for pixel in tree:
    pixel.color = (1, 0, 0)
    sleep(1)
```

To control a specific pixel, you can access it by its index number (0-24):

```python
tree[0].color = (0, 1, 0)
```

## Random sparkles

To randomly colour all the LEDs repeatedly, you need to set the value of the
whole tree to a list of 25 random colour values. Start by writing a function to
generate a random colour:

```python
from random import random

def random_color():
    r = random()
    g = random()
    b = random()
    return (r, g, b)
```

Then create a second function to create a list of 25 random colours:

```python
from random import random

def random_colors(n):
    return [random_color() for i in range(n)]
```

Now write a loop to set the tree's value to this list:

```python
while True:
    tree.value = random_colors(25)
```
