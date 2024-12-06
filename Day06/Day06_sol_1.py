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
visited = []

def hasEscaped(curr_pos):
    x, y = curr_pos
    return not (0 <= x < MAX_WIDTH and 0 <= y < MAX_HEIGHT)

def calc_direction(curr_pos, direction, mapp=input_data):
    x, y = curr_pos
    _visited = []
    deltas = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}
    dx, dy = deltas[direction]
    
    while 0 <= x < MAX_WIDTH and 0 <= y < MAX_HEIGHT:
        if mapp[y][x] != BLOCKER:
            _visited.append((x, y))
            x += dx
            y += dy
        else:
            x -= dx 
            y -= dy 
            break
    return _visited, (x, y)

direction = {"^" : "up",
             ">" : "right",
             "<" : "left",
             "v" : "down"}
rotation_seq = ["^", ">", "v", "<"]

currDir = "^" # "^" taken by looking at the input file

currDirIndex = "".join(rotation_seq).index(currDir)
firstEncounterIndex = "".join(input_data).index(currDir) 
curr_pos = (firstEncounterIndex%MAX_WIDTH, firstEncounterIndex//MAX_WIDTH)

countt = 0
while not hasEscaped(curr_pos):
    _visited = []
    _visited, curr_pos = calc_direction(curr_pos, direction[currDir])
    visited += _visited
    currDirIndex = (currDirIndex+1)%len(rotation_seq)
    currDir = rotation_seq[currDirIndex]
visited = list(set(visited))
print(len(visited)) 
# 4778