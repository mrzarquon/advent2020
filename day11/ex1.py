#!/usr/bin/env python3
import os
import sys
import re
import operator
import numpy
import scipy
from copy import deepcopy
from pprint import pprint

seats = open(sys.argv[1],"r").readlines()

seats = [list(i.rstrip('\n')) for i in seats]

empty = ['L']
full = ['#']

original = deepcopy(seats)

# all squares around x,y
directions = [(-1,-1),(0,-1),(+1,-1) ,(-1,0),(+1,0),(-1,+1),(0,+1),(+1,+1)]
# this is a list of x,y coordinates what we want to swap whatever is in the seat

minX = 0
maxX = len(seats[0])
minY = 0
maxY = len(seats)

def checkX(x,dx):
    offset = x + dx
    if offset < minX or offset >= maxY:
        return False
    else:
        return True

def checkY(y,dy):
    offset = y + dy
    if offset < minY or offset >= maxY:
        return False
    else:
        return True

def scan(m, x, y):
    count = 0
    for d in directions:
        dx,dy = d
        if checkX(x,dx) and checkY(y,dy):
            if m[y+dy][x+dx] in full:
                count += 1
        else:
            pass
    return count

def parseSeats(seats):
    seatsToSwap = list()
    for ypos in range(maxY):
        for xpos in range(maxX):
            seat = seats[ypos][xpos]
            if seat != '.':
                fullseats = scan(seats,xpos,ypos)
                if fullseats >= 4 and seat in full:
                    # make it empty
                    seatsToSwap.append((ypos,xpos))
                elif fullseats == 0 and seat in empty:
                    seatsToSwap.append((ypos,xpos))

    for swaps in seatsToSwap:
        dy,dx = swaps
        if seats[dy][dx] in full:
            seats[dy][dx] = 'L'
        elif seats[dy][dx] in empty:
            seats[dy][dx] = '#'

    return(len(seatsToSwap))

def countSeats(seats):
    count = 0
    for ypos in range(maxY):
        for xpos in range(maxX):
            seat = seats[ypos][xpos]
            if seat in full:
                count += 1
    return count

swapToDo = 1
totalSwaps = 0
while swapToDo != 0:
    swapToDo = parseSeats(seats)
    totalSwaps += 1

print('p1 occupied seats:',countSeats(seats))

# reset for p2


#pprint(original)

def scanSight(m, x, y):
    count = 0
    for d in directions:
        dx,dy = d
        ty = y + dy
        tx = x + dx
        while 0 <= tx < maxX and 0 <= ty < maxY:
            if m[ty][tx] != '.':
                if m[ty][tx] in full:
                    count += 1
                break
            tx += dx
            ty += dy
    return count

def parseSeatsSight(zed):
    seatsToSwap = list()
    for ypos in range(maxY):
        for xpos in range(maxX):
            seat = zed[ypos][xpos]
            if seat != '.':
                fullseats = scanSight(zed,xpos,ypos)
                if fullseats >= 5 and seat in full:
                    # make it empty
                    seatsToSwap.append((ypos,xpos))
                elif fullseats == 0 and seat in empty:
                    seatsToSwap.append((ypos,xpos))

    for swaps in seatsToSwap:
        dy,dx = swaps
        if zed[dy][dx] in full:
            zed[dy][dx] = 'L'
        elif zed[dy][dx] in empty:
            zed[dy][dx] = '#'

    return(len(seatsToSwap))

#pprint(original)

swapToDo = 1
totalSwaps = 0
while swapToDo != 0:
    swapToDo = parseSeatsSight(original)
    totalSwaps += 1

print('p2 occupied seats:',countSeats(original))