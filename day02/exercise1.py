#!/usr/local/bin/python3

# 13-16 k: kkkkkgmkbvkkrskhd
# 5-6 p: qpppvzp
# 3-4 p: psppxhlfpvkh

# explode 
# ['9-12', 'c:', 'pccvnbccxrncrcclccc']
# ['14-18', 's:', 'ssssssssslsssstsssss']

def verify(raw: str):
    explode = raw.strip().split()
    g = int(explode[0].split('-')[0])
    l = int(explode[0].split('-')[1])
    c = explode[1][0]
    t = explode[2].count(c)
    if (t >= g and t <= l ):
        return True
    else:
        return False

inFile = open("input.txt","r").readlines()

print(len(inFile))

inFile = [ i for i in inFile if verify(i) ]

print(len(inFile))