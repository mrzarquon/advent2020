#!/usr/bin/env python3
import os
import sys
import re
import operator
from pprint import pprint

inst = open(sys.argv[1],"r").readlines()

acc = 0
loc = 0

ops = { "+": operator.add, "-": operator.sub }

def jump(arg: str, loc: int):
    #print('jmp:', arg)
    x = arg[0]
    y = int(arg[1:])
    loc = ops[x](loc,y)
    return loc


def accumulate(arg: str, acc: int):
    #print('acc:', arg)
    x = arg[0]
    y = int(arg[1:])
    acc = ops[x](acc,y)
    return acc


def swap(action):
    if action == 'nop':
        return 'jmp'
    elif action == 'jmp':
        return 'nop'
    else:
        return action

def testInstructions(z,swapLoc):
    loc_log = list()
    acc = 0
    loc = 0
    while loc not in loc_log and loc < len(z):
        loc_log.append(loc)
        p = z[loc].split(' ')
        
        if loc == swapLoc:
            action = swap(p[0])
        else:
            action = p[0]
    

        if action == 'nop':
            loc += 1
        elif action == 'acc':
            acc = accumulate(p[1].rstrip('\n'), acc)
            loc += 1
        elif action == 'jmp':
            loc = jump(p[1].rstrip('\n'),loc)
    
    if loc in loc_log:
        loop = True
    elif loc >= len(z):
        loop = False

    #print('loc:',loc,'acc:',acc,'last_line:',loc_log[-1]+1)
    return loop,acc

#print(testInstructions(inst))

jmpLoc = [i for i, s in enumerate(inst) if 'jmp' in s]
nopLoc = [i for i, s in enumerate(inst) if 'nop' in s]
testLoc = jmpLoc + nopLoc

for test in range(0,len(testLoc)):
    isLoop,count = testInstructions(inst,testLoc[test])

    if isLoop:
        foo = 0
        #print(testLoc[test],'not work')
    else:
        print(testLoc[test],'fixed it',count)


