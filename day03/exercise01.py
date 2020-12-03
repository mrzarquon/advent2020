#!/usr/bin/env python3

inFile = open("input.txt","r").readlines()

inFile = [i.strip() for i in inFile]

values = {
  "test1": [1,1,0],
  "test2": [3,1,0],
  "test3": [5,1,0],
  "test4": [7,1,0],
  "test5": [1,2,0]
}

total = 1

def findTrees (X: int, Y: int, inFile):
  #print(len(inFile))
  trees = 0
  for location in range(0,len(inFile),Y):
    #print(location)
    line = location
    pointer = (location * X) % 31
    #print(inFile[line][pointer])
    if inFile[line][pointer] == '#':
      trees += 1
  #print(trees)
  return trees

for test in values:
  print(values[test])
  X = values[test][0]
  Y = values[test][1]
  values[test][2] = findTrees(X, Y, inFile)
  total = total * values[test][2]

print(values)
print(total)

print(104*230*83*98*50)

# line 0, space 0
# line 1, space 3
# line 2, space 6
# line 3, space 9
# line 4, space 12
# line 5, space 15
# line 6, space 18
# line 10, space 30
# line 11, space 33

#location = counter % 31

