#!/usr/bin/env python3

inFile = open("input.txt","r").readlines()

inFile = [i.strip() for i in inFile]

slopes = {
  "test1": {
    'x': 1,
    'y': 1,
    'trees': 0
  },
  "test2":{
    'x': 3,
    'y': 1,
    'trees': 0
  },
  "test3": {
    'x': 5,
    'y': 1,
    'trees': 0
  },
  "test4": {
    'x': 7,
    'y': 1,
    'trees': 0
  },
  "test5": {
    'x': 1,
    'y': 2,
    'trees': 0
  }
}

def findTrees (X: int, Y: int, inFile):
  trees = 0
  # while we could use the iterator, for slope5 we only move 1 space to the right
  # for every 2 steps down
  step = 0
  # we want a number instead of the object itself
  for line in range(len(inFile)):
    # first we want to make sure we're on a line that we've not skipped
    # if we're meant to increment by 2, then any line number divisble by 2 is
    # where we can land, same for three, so if there's no remainder, then bingo
    if (line % Y == 0):
      # since the pattern returns every 31 characters we only care about the
      # where in a row of 31 we land, which is the how many steps we taken
      # multiplied by our offset, and then find what wasn't a complete iteration
      # of 31 steps (aka the remainder)
      pos = (step * X) % 31
      step += 1
      
      # If that character is a # it means we hit a tree 
      if inFile[line][pos] == '#':
        trees += 1
  
  return trees

# here we're just getting the key names so we can reference back 
# to the original hash and not have to pass it back and forth

for s in slopes:
  X = slopes[s]['x']
  Y = slopes[s]['y']
  slopes[s]['trees'] = findTrees(X, Y, inFile)
  #total = total * values[test][2]

total = 1

# here we're calling the subhashes which are the values of the first level keys
# to save typing
for t in slopes.values():
  total = total * t['trees']

print(total)
