# one to read thought later

delta_force = [complex(x,y) for x in (-1,0,1) for y in (-1,0,1) if not x==y==0]

def neighbors(floor,loc,queen):
    for delta in delta_force:
        nloc = loc + delta
        while queen and nloc in floor and floor[nloc] == '.': nloc = nloc + delta
        if nloc in floor and floor[nloc]=='#': yield 1

def part(p, new_floor, floor = None):
    while floor != new_floor:
        floor = new_floor.copy()
        for loc in ( x for x in floor if floor[x] != '.' ):
            n = sum(neighbors(floor,loc,p))
            if n > (3+p): new_floor[loc] = 'L'
            elif n == 0: new_floor[loc] = '#'
    print(f'part {p+1}: {sum(cell=="#" for cell in new_floor.values())}')

lines = ( list(s.strip()) for s in open(day_11_path).readlines() )
lines = { complex(x,y): cell for x,row in enumerate(lines) for y,cell in enumerate(row) }
part(0,lines.copy())

part(1,lines.copy())
