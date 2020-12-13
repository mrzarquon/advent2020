#!/usr/bin/env python3
import os
import sys
import re
import operator
from copy import deepcopy
from pprint import pprint

nav = open(sys.argv[1],"r").readlines()

nav = [(i.rstrip('\n')[0],int(i.rstrip('\n')[1:])) for i in nav]

print(nav)

CARD = ['N','E','S','W']

pos = {
    'x': 0,
    'y': 0,
    'h': 'E'
}

def changeHeading (heading, direction, turn):
    turns = turn / 90
    if direction == 'L':
        direction = -1
    elif direction == 'R':
        direction = +1
    
    turns = turns * direction

    headPos = CARD.index(heading)

    headPos = int((headPos + turns) % len(CARD))

    return CARD[headPos]

def changePosition (pos, compass, moves):
    # if south or west, we move negative
    if compass == CARD[0]:
        axis = 'y'
    elif compass == CARD[1]:
        axis = 'x'
    elif compass == CARD[2]:
        moves = moves * -1
        axis = 'y'
    elif compass == CARD[3]:
        moves = moves * -1
        axis = 'x'

    pos[axis] += moves

    return pos

for line in nav:
    print(pos)
    if line[0] in CARD:
        print('we are moving in a direction',line[0])
        pos = changePosition(pos, line[0], line[1])
    elif line[0] == 'F':
        pos = changePosition(pos, pos['h'], line[1])
    else:
        print('we are turning',line[0])
        pos['h'] = changeHeading(pos['h'],line[0], line[1])
    
    print(pos)
    




