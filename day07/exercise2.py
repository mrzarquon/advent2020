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



def countBags(rule,bag):
    enclosedBags = 0
    if bool(rule[bag]):
        print(bag,'has bags')
        for enBag in rule[bag]:
            mult = rule[bag][enBag]
            count = countBags(rule,enBag)
            enclosedBags += mult * count

    if bag == 'shinygold':
        return enclosedBags
    else:
        return enclosedBags + 1

print(countBags(rules,'shinygold'))
