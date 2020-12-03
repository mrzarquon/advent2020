#!/usr/bin/env python3

inFile = open("input.txt","r").readlines()

inFile = [i.strip() for i in inFile]

pointer = 0
trees = 0
for location in range(0,len(inFile),1):
  line = location
  pos = (pointer * 1) % 31
  if (line % 2 == 0):
    pointer += 1
    if inFile[line][pos] == '#':
      marked = inFile[line][0:pos] + 'X' + inFile[line][pos+1:]
      trees += 1
    else:
      marked = inFile[line][0:pos] + 'O' + inFile[line][pos+1:]
  else:
    marked = inFile[line]
  
  print(f"{line:03d}", ": ", inFile[line], " : ", marked)

print(trees)

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

