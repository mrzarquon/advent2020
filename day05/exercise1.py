#!/usr/bin/env python3
import os
import sys
import re
from pprint import pprint

inFile = open(sys.argv[1],"r").readlines()

def strip(string: str):
  return string.rstrip('\n')

def binarySort(record, upper: int, zero: str, one: str):
  steps = list(record)

  row = range(0,upper)
  for step in steps:
    if step == zero:
      row = row[:len(row)//2]
    elif step == one:
      row = row[len(row)//2:]
  
  return row[0]

#

def findMissing(seats):
  for i in range(0,len(seats)):
    try:
      seats[i]
    except KeyError:
      print(i,' is missing')


inFile = list(map(strip,inFile))

#    BFFFBBFRRR: row 70, column 7, seat ID 567.
#    FFFBBBFRRR: row 14, column 7, seat ID 119.
#    BBFFBBFRLL: row 102, column 4, seat ID 820.

seats = dict()
highSeat = 0
for seat in inFile:
  row = binarySort(seat[0:7],128,'F','B')
  col = binarySort(seat[7:10],8,'L','R')
  seatID = (row * 8) + col
  seats[seatID] = [row,col]
  if seatID > highSeat:
    highSeat = seatID

print(len(seats))

pprint(highSeat)

findMissing(seats)