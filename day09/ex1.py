#!/usr/bin/env python3
import os
import sys
import re
import operator
from pprint import pprint

preamble = open(sys.argv[1],"r").readlines()

lookback = int(sys.argv[2])

#[i for i, s in enumerate(inst) if 'jmp' in s]

preamble = [int(i.strip()) for i in preamble]

def findSum(theList,target):
  sums = [(x,y) for x in theList for y in theList if (x + y == target) and x != y]
  return sums

#results = [(x,y) for x in inFile for y in inFile if (x + y == 2020)]

answer = 0
answerLoc = 0

for x in range(lookback,len(preamble)):
  start = x - lookback
  end = x
  target = preamble[x]
  theList = preamble[start:end]
  results = findSum(theList,target)
  if bool(results) == False:
    print(preamble[x],'breaks rule')
    answer = preamble[x]
    answerLoc = x
