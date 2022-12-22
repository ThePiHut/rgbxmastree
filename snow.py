from tree import RGBXmasTree
import random
from time import sleep
from itertools import count, cycle

P_NEW_ROUTE = 0.5
P_MOVE = 1
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
    x = None
    for y in route:
        yield x, y
        x = y
    yield y, None

def turn_on(x):
    if x is not None:
        tree[x].color = (10, 10, 10)
        
def turn_off(x):
    if x is not None:
        tree[x].color = (0, 0, 0)


current_routes = {}
next_index = cycle(count(1000000))
while True:
    if random.random() < P_NEW_ROUTE:
        current_routes[next(next_index)] = gen(routes[random.randrange(8)])

    for k in sorted(current_routes.keys()):
        if random.random() < P_MOVE:
            last, new = next(current_routes[k])
            turn_off(last)
            turn_on(new)
            if new is None:
                del current_routes[k]

    sleep(SLEEP)
