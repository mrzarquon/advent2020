#!/usr/bin/env python3

import os
import sys
import pandas as pd
import re
from pprint import pprint

inFile = open(sys.argv[1],"r").readlines()


p = list()
p.append(list())

for line in inFile:
    if len(line) > 2:
        p[-1].append(line.replace('\n',' '))
    else:
        p.append(list())

# i'm sure there's a single regex for all this
for i in range(0,len(p)):
    p[i] = ''.join(p[i])
    p[i] = p[i].rstrip()
    p[i] = dict(subStr.split(':') for subStr in p[i].split(' '))

df = pd.DataFrame(p, columns = ['byr','cid','ecl','eyr','hcl','hgt','iyr','pid'])

df.dropna(subset=['byr','ecl','eyr','hcl','hgt','iyr','pid'], inplace=True)

objectTypes = {
    'byr': int,
    'eyr': int,
    'iyr': int,
    'pid': str,
    'hcl': str,
    'ecl': str,
    'hgt': str
}

df = df.astype(objectTypes, errors='ignore')

print('part 1: ', df.shape[0])

def validRange(year, minY: int, maxY: int):
    try:
        year = int(year)
        if year >= minY and year <= maxY:
            return True
        else:
            return False
    except ValueError:
        return False

def validEyes(eye):
    eyecolors = ['amb','blu','brn','gry','grn','hzl','oth']
    try:
        eye = str(eye)
        if eye in eyecolors:
            return True
        else:
            return False
    except ValueError:
        return False

pattern = re.compile("^([a-z0-9]+)$")

def validHair(hair):
    try:
        hair = str(hair)
        if hair[0] == '#' and len(hair) == 7:
            if pattern.search(hair[1:6]):
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False

def validHeight(hgt):
    try:
        if hgt[-2:] == 'cm':
            hgt = int(hgt[:-2])
            if hgt >= 150 and hgt <= 193:
                return True
            else:
                return False
        elif hgt[-2:] == 'in':
            hgt = int(hgt[:-2])
            if hgt >= 59 and hgt <= 76:
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False


pidpat = re.compile("^([0-9]+)$")
def validPid(pid):
    try:
        pid = str(pid)
        if len(pid) == 9:
            if pidpat.search(pid):
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False

df = df[df.byr.apply(validRange, minY=1920, maxY=2002)]
df = df[df.iyr.apply(validRange, minY=2010, maxY=2020)]
df = df[df.eyr.apply(validRange, minY=2020, maxY=2030)]
df = df[df.ecl.apply(validEyes)]
df = df[df.hcl.apply(validHair)]
df = df[df.hgt.apply(validHeight)]
df = df[df.pid.apply(validPid)]

pprint(df)

print('part 2: ', df.shape[0])