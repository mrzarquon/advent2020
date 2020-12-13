#!/usr/bin/env python3
import os
import sys
import re
import operator
from pprint import pprint

# knights dialer: https://hackernoon.com/google-interview-questions-deconstructed-the-knights-dialer-f780d516f029

adp = open(sys.argv[1],"r").readlines()

adp = [int(i.strip()) for i in adp]

adp.append(0)

adp = sorted(adp)

adp.append(adp[-1]+3)

j1 = 0
j3 = 0
for i in range(1,len(adp)):
    try:
        jolts = adp[i] - adp[i-1]
        if jolts == 1:
            j1 += 1
        elif jolts == 3:
            j3 += 1
        #print(i,adp[i],adp[i+1],jolts,j1,j3)
    except IndexError:
        print('end')

print(len(adp))
# copied from elsehwere, annoyed i didn't notice this
arrangements = [1]
for i in range(1, len(adp)):
    # take the last arrangement
    arrange = arrangements[i-1]
    j = i - 2
    print(arrange, adp[i], adp[j])
    print(arrangements)
    # walk the adapters
    # 
    while j >= 0 and adp[i] - adp[j] <= 3:
        # if the difference in joules is 3,2,1,0
        arrange += arrangements[j];
        print('++',arrangements[j],j,arrange,adp[i],adp[j])
        j -= 1
        print(arrangements)

    arrangements.append(arrange);

print(len(arrangements))
print(arrangements[-1])

pattern = list()
for i,n in zip(adp,adp[1:]):
    pattern.append(n-i)

print(pattern)
paths = [1,1]
for x,y,a,b in zip(pattern, pattern[1:], paths, paths[1:]):
    # save the count here (we want the last path)
    count = b
    if x == 1 and y == 1:
        count = count + a
    # save our double
    paths.append(count)
    print(paths)

print(paths)