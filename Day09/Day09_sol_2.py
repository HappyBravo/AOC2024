from collections import defaultdict 

input_file = "Day09_input.txt"
input_data = []

with open(input_file, "r") as f:
    input_data = [_.strip() for _ in f.readlines()]

test = """\
2333133121414131402"""
# input_data = [_.strip() for _ in test.splitlines()]

def checksum(line):
    line = line.split()
    summ = 0
    for i, num in enumerate(line):
        if num != ".":
            summ += i*int(num) 
    return summ 

def lineMaker(digits):
    spaces = defaultdict(list)
    digits = list(digits)
    line, prevSumm= "", 0
    for i, num in enumerate(digits):
        _spaces = []
        num = int(num)
        fragment = ""
        if i%2:
            fragment = ". "*num
            _spaces = [_ for _ in range(prevSumm, prevSumm+num)]
            if _spaces:
                spaces[len(_spaces)].append((_spaces[0], _spaces[-1]))
        else:
            fragment = f"{f'{i//2} '*num}"
        line += fragment
        prevSumm += num
    return line, spaces 

def _swapper(line, spacePos = [], blockPos = []):
    if (len(spacePos) == len(blockPos)) and spacePos[-1] < blockPos[0]:
        for i, _ in enumerate(spacePos):
            line[spacePos[i]], line[blockPos[i]] = line[blockPos[i]], line[spacePos[i]]
    return line

def defragmenter(line, spaces):
    line = list(line.split())
    left, right = len(line)-1, len(line)-1
    while left > 0:
        if line[right] != ".":
            if line[left] == line[right]:
                left -=  1
                continue
            else:
                filePos = list(range(left+1, right+1))
                lenFile = len(filePos)
                possSpaces = [_ for _ in sorted(spaces, key = lambda k: min([x for x, y in spaces[k]], default=0)) 
                                                if _ >= lenFile and spaces[_]]
                if not possSpaces:
                    right, left = left, left - 1
                    continue
                for _lenFile in possSpaces:
                    _spaces = spaces[_lenFile]  # TAKE OUT ALL COORDINATES 
                    _blankPos = _spaces[0]  # TAKE THE FIRST ELEMENT FROM THE LIST
                    spacesToSwap = list(range(_blankPos[0], _blankPos[1]+1))
                    if lenFile != _lenFile: # IF lenFile < _lenFile
                        diff = abs(lenFile - _lenFile)
                        _spacesToSwap = spacesToSwap[:lenFile]  # ONLY THESE POSITIONS NEED TO BE SWAPPED
                        diffPos = spacesToSwap[lenFile:]    # THESE POSITIONS ARE TO BE LEFT BLANK
                        spaces[diff].append((diffPos[0], diffPos[-1]))  # UPDATE THE spaces DICTIONARY 
                        spaces[diff] = sorted(spaces[diff])
                        spacesToSwap = _spacesToSwap
                    spaces[_lenFile] = _spaces[1:]
                    line = _swapper(line, spacesToSwap, filePos)
                    right = left
                    break
                left -= 1
        else:
            right, left = right - 1, left - 1
    return " ".join(line)
print(checksum(defragmenter(*lineMaker(input_data[0]))))
# 6398065450842