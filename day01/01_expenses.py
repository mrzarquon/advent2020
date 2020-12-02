#!/usr/bin/env python3

inFile = open("input.txt","r").readlines()

inFile = [int(i.strip()) for i in inFile]

print(inFile)

results = [(x,y) for x in inFile for y in inFile if (x + y == 2020)]

print(results[0])

intX,intY = results[0]

final = intX * intY

print(final)

# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

harder = [(x * y * z) for x in inFile for y in inFile for z in inFile if (x + y + z == 2020)]

print(harder)