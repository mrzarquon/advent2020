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
TURN = ['L','R']

pos = {
    'x': 0,
    'y': 0,
    'h': 'E'
}

wayPoint = {
    'x': 10,
    'y': 1,
    'h': 'E'
}

def changeHeading (wayPoint, direction, turn):
    turns = int(turn / 90)
    
    x = wayPoint['x']
    y = wayPoint['y']

    for i in range(0,turns):
        print('turn number', i)
        if direction == 'R':
            x,y = turnRight(x,y)
        else:
            x,y = turnLeft(x,y)
    
    wayPoint['x'] = x
    wayPoint['y'] = y

    return wayPoint


def turnRight(x,y):
    newX = y
    newY = x * -1
    return newX,newY

def turnLeft(x,y):
    newX = y * -1
    newY = x
    return newX,newY

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

def changeWay(wayPoint, compass, moves):
    if compass in TURN:
        wayPoint = changeHeading(wayPoint, compass, moves)
        return wayPoint
    else:
        wayPoint = changePosition(wayPoint, compass, moves)
        return wayPoint

def moveShip(pos, wayPoint, moves):
    shipX = pos['x']
    wayX = wayPoint['x']
    shipY = pos['y']
    wayY = wayPoint['y']

    shipX += wayX * moves
    shipY += wayY * moves

    pos['x'] = shipX
    pos['y'] = shipY

    return pos


for line in nav:
    print(pos)
    if line[0] in CARD or line[0] in TURN:
        print('we are moving waypoint',line[0])
        wayPoint = changeWay(wayPoint, line[0], line[1])
    elif line[0] == 'F':
        print('we are moving ship forward',line[1])
        pos = moveShip(pos, wayPoint, line[1])
    
    print(pos)

manX = abs(pos['x'])
manY = abs(pos['y'])

print('manhattan:', manX,'+',manY,'=',manX+manY)