#!/usr/bin/env python3
import os
import sys
import re
from pprint import pprint

bagRules = open(sys.argv[1],"r").readlines()

rules=dict()
for bag in bagRules:
    bag = bag.split(' ')
    rules[bag[0]+bag[1]] = dict()
    rules[bag[0]+bag[1]]['rule'] = bag[4:]

def parseRule(r):
    p = dict()
    if r[0] == 'no':
        return dict()
    else:
        for x in range(0,len(r),4):
            name = r[x+1]+r[x+2]
            quantity = r[x]
            p[name] = int(quantity)
        return p

# keeps the hash
#for key in rules:
#    rules[key]['parsed'] = parseRule(rules[key]['rule'])

for key in rules:
    parsed = parseRule(rules[key]['rule'])
    rules[key] = parsed

bags = ['shinygold']
for bag in bags:
    for rule in rules:
        if any(bag in x for x in rules[rule]):
            print(rule)
            bags.append(rule)

print(bags)
results = sorted(set(bags))
print(len(results)-1)