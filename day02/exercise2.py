#!/usr/local/bin/python3

# 13-16 k: kkkkkgmkbvkkrskhd
# 5-6 p: qpppvzp
# 3-4 p: psppxhlfpvkh

# explode 
# ['9-12', 'c:', 'pccvnbccxrncrcclccc']
# ['14-18', 's:', 'ssssssssslsssstsssss']

def verify(raw: str):
    #print(raw.strip())
    explode = raw.strip().split()
    #print(explode)
    # now we're doing strings so shift left
    g = int(explode[0].split('-')[0]) - 1
    l = int(explode[0].split('-')[1]) - 1 
    c = explode[1][0]
    p = explode[2]
    # i misread and it's either place but never both or never not
    if ( (c == p[g] and c != p[l]) or (c != p[g] and c == p[l]) ):
        return True
    else:
        #print("c: %s g: %s l: %s" % (c, p[g], p[l]) )
        return False

inFile = open("input.txt","r").readlines()

print(len(inFile))

inFile = [ i for i in inFile if verify(i) ]

print(len(inFile))
