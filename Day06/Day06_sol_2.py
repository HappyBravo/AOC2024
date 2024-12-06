input_file = "Day06_input.txt"
input_data = []

with open(input_file, "r") as f:
    input_data = [_.strip() for _ in f.readlines()]

test = \
"""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
# input_data = [_.strip() for _ in test.splitlines()]

MAX_HEIGHT, MAX_WIDTH = len(input_data), len(input_data[0])
BLOCKER = "#"

directions = {"^" : "up",
             ">" : "right",
             "<" : "left",
             "v" : "down"}
rotation_seq = ["^", ">", "v", "<"]
deltas = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}

starting_dir = "^" # "^" taken by looking at the input file
startingDirIndex = "".join(rotation_seq).index(starting_dir)
firstEncounterIndex = "".join(input_data).index(starting_dir) 
starting_pos = (firstEncounterIndex%MAX_WIDTH, firstEncounterIndex//MAX_WIDTH)
startingState = (starting_pos, directions[starting_dir])

obsPosToCheck = [(x,y) for y, ys in enumerate(input_data) for x, xs in enumerate(ys) if xs == "."]
# print(len(obsPosToCheck))

visited = []
countt = 0
for obs_pos in obsPosToCheck:
    print(f"obstacle at - {obs_pos}", end = " ")
    x, y = starting_pos
    currDir = starting_dir
    direction = directions[currDir]
    currDirIndex = startingDirIndex
    visited = set()
    _mapp = input_data[:]
    _mapp[obs_pos[1]] = _mapp[obs_pos[1]][:obs_pos[0]] + BLOCKER + _mapp[obs_pos[1]][obs_pos[0]+1:]
    while (0 <= x < MAX_WIDTH and 0 <= y < MAX_HEIGHT):
        direction = directions[currDir]
        dx, dy = deltas[direction]
        currState = ((x, y), direction)
        # print(f"Current : {(x,y)} \nVisited : {visited}\nNew visited : {currState}")
        if _mapp[y][x] != BLOCKER:
            if currState in visited and currState != startingState:
                print(f"--- LOOP FOUND", end = " ")
                countt += 1
                break
            visited.add(((x, y), direction))
            x, y = x+dx, y+dy
        else :
            x, y = x-dx, y-dy  
            currDirIndex = (currDirIndex+1)%len(rotation_seq)
            currDir = rotation_seq[currDirIndex]
    print()
print(countt)
# 1618
