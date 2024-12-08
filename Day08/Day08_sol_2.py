from collections import defaultdict

input_file = "Day08_input.txt"
input_data = []

with open(input_file, "r") as f:
    input_data = [_.strip() for _ in f.readlines()]

test = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

test2 = """\
T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
.........."""

# input_data = [_.strip() for _ in test.splitlines()]
# input_data = [_.strip() for _ in test2.splitlines()]

MAX_HEIGHT, MAX_WIDTH = len(input_data), len(input_data[0])
ant_chars = []
ant_chars += [chr(_) for _ in range(ord('a'), ord('z')+1)] \
            + [chr(_).upper() for _ in range(ord('a'), ord('z')+1)] \
            + list(map(str, range(10)))

ant_coor_dict = defaultdict(list)
[ant_coor_dict[xs].append((x,y)) for y, ys in enumerate(input_data) 
                                        for x, xs in enumerate(ys) if xs if xs in ant_chars]

antinodes = set()
for ant, coors in ant_coor_dict.items():
    for i, coor1 in enumerate(coors[:]):
        for j, coor2 in enumerate(coors[i:]):
            print(f"Checking {coor1, coor2}")
            (x1, y1), (x2, y2) = sorted([coor1, coor2])
            dx, dy, dirr = abs(x1 - x2), \
                           abs(y1 - y2), \
                           (y1-y2)/abs(y1-y2) if y1-y2 !=0 else 1
            _antinodes = [((x1-z*dx, int(y1+(z*dirr*dy))), (x2 + z*dx, int(y2-(z*dirr*dy)))) 
                                                        for z in range(1, MAX_HEIGHT)]
            [antinodes.add((x,y)) for _cs in _antinodes 
                                        for (x,y) in _cs 
                                        if 0 <= x < MAX_WIDTH and 0 <= y < MAX_HEIGHT]
print(len(antinodes))
# 905