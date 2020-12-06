#!/usr/bin/env python3
import os
import sys
import re
from pprint import pprint

inFile = open(sys.argv[1],"r")

customs = inFile.read().split('\n\n')

groups = dict()
for x in range(0,len(customs)):
    groups[x] = { 'form' : customs[x].split('\n') }

test = ['ab', 'ac']

def squash(arr):
    arr = set(arr)
    arr = sorted(arr)
    return arr

def explode(arr):
    c = list()
    for a in arr:
        for b in a:
            c.append(b)
    print(c)
    return c


def findCommon(arr):
    y = dict()
    z = list()
    # arr = ['ab', 'ac']
    for c in arr:
        # c = 'ab'
        for d in c:
            print(d)
            if d in z:
                print('match')
                y[d] += 1
            else:
                y[d] = 1
                z.append(d)
    
    return y

def findMatch(dicc, size):
    print(dicc,size)
    return dict(filter(lambda elem: (elem[1] % size == 0),dicc.items()))



#print(findCommon(test))

#matched = list(filter(lambda x : len(x) == 2 , findCommon(test)))

#print(matched)


total = 0
for x in range(0,len(groups)):
    groups[x]['sorted'] = squash(explode(groups[x]['form']))
    groups[x]['count'] = len(groups[x]['sorted'])
    groups[x]['common'] = findCommon(groups[x]['form'])
    groups[x]['matches'] = findMatch(groups[x]['common'],len(groups[x]['form']))
    total += len(groups[x]['matches'])

pprint(groups)
pprint(total)

# if character not in list = append, if in list, add?
# then find number of characters of len = group?