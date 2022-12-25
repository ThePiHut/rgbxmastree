from tree import RGBXmasTree
import random
from time import sleep
from itertools import count, cycle

P_NEW_ROUTE = 0.3333333
SLEEP = 1

tree = RGBXmasTree()
tree.brightness = 0.1
tree[3].color = (10, 10, 10)

routes = [
    [2, 1, 0],
    [4, 5, 6],
    [9, 8, 7],
    [10, 11, 12],
    [13, 14, 15],
    [18, 17, 16],
    [21, 20, 19],
    [22, 23, 24]
]

def gen(route):
    for y in route:
        yield y
    yield None

def turn_on(x):
    if x is not None:
        tree[x].color = (10, 10, 10)
        
def turn_off(x):
    if x is not None:
        tree[x].color = (0, 0, 0)


current_routes = {}
next_index = cycle(count(1000000))
while True:
    new_lights = [(0, 0, 0)] * 25
    new_lights[3] = (1, 1, 1)
    for r in routes:
        if random.random() < P_NEW_ROUTE:
            current_routes[next(next_index)] = gen(r)

    for k in sorted(current_routes.keys()):
        new = next(current_routes[k])
        if new is None:
            del current_routes[k]
        else:
            new_lights[new] = (1, 1, 1)
    tree.value = new_lights
    sleep(SLEEP)
