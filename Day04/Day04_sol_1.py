input_file = "Day04_input.txt"
input_data = []

with open(input_file, "r") as f:
    input_data = [_.strip() for _ in f.readlines()]

test = \
"""
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
# input_data = [_.strip() for _ in test.splitlines() if _]

TO_FIND = "XMAS"

MAPP_HEIGHT, MAPP_WIDTH = len(input_data), len(input_data[0])
print(len(input_data), len(input_data[0]))

def move(x, y, dx, dy, max_x, max_y):
    if x is None or y is None:
        return None, None
    if not (0 <= (x + dx) and (x + dx) < max_x and 0 <= (y + dy) and (y + dy) < max_y):
        return None, None
    return x + dx, y + dy

def up(x, y):
    return move(x, y, 0, -1, MAPP_WIDTH, MAPP_HEIGHT)

def down(x, y):
    return move(x, y, 0, 1, MAPP_WIDTH, MAPP_HEIGHT)

def right(x, y):
    return move(x, y, 1, 0, MAPP_WIDTH, MAPP_HEIGHT)

def left(x, y):
    return move(x, y, -1, 0, MAPP_WIDTH, MAPP_HEIGHT)

def diag(x, y, upp=0):
    return left(*up(x, y)) if upp else right(*down(x, y))

def off_diag(x, y, upp=0):
    return right(*up(x, y)) if upp else left(*down(x, y))

def get_next3(x, y):
    toMove = 3
    ups, downs, lefts, rights, diags, diag_ups, offdiags, offdiag_ups = [(x,y)], [(x,y)], [(x,y)], [(x,y)], [(x,y)], [(x,y)], [(x,y)], [(x,y)]
    for i in range(toMove):
        ups.append(up(*ups[i]))
        downs.append(down(*downs[i]))
        
        lefts.append(left(*lefts[i]))
        rights.append(right(*rights[i]))
        
        diags.append(diag(*diags[i]))
        diag_ups.append(diag(*diag_ups[i], upp=1))

        offdiags.append(off_diag(*offdiags[i]))
        offdiag_ups.append(off_diag(*offdiag_ups[i], upp=1))

    return {'up' : ups[1:],
            'down' : downs[1:], 
            'left' : lefts[1:], 
            'right' : rights[1:], 
            'diag' : diags[1:], 
            'diag_up' : diag_ups[1:],
            'offdiag' : offdiags[1:],
            'offdiag_up' : offdiag_ups[1:]}

directions = ['up', 'down', 'right', 'left', 'diag', 'diag_up', 'offdiag', 'offdiag_up']

def getCharFromPos(x, y=None):
    # print(x, y)
    if isinstance(x, tuple):
        (x, y) = x
        # print(x, y)
    assert x != None and y != None 
    return input_data[y][x]

countt = 0
for y in range(MAPP_HEIGHT):
    for x in range(MAPP_WIDTH):
        if input_data[y][x] == 'X':
            # print(y, x)
            neighbours = get_next3(x, y)
            # print(neighbours)
            # input()
            for direction in directions:
                if not all([_x != None and _y != None for (_x,_y) in neighbours[direction]]):
                    # print(f"{neighbours[direction]} One contain None, None")
                    # input()
                    continue
                if f"X{''.join(map(getCharFromPos, neighbours[direction]))}" == TO_FIND:
                    print(y, x, f"found XMAS in {direction}")
                    countt +=1 
            # input()
print(countt)
# 2603 