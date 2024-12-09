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
    digits = list(digits)
    line = ""
    for i, num in enumerate(digits):
        num = int(num)
        fragment = ""
        if i%2 :
            fragment = ". "*num
        else:
            fragment = f"{f'{i//2} '*num}"
        line += fragment
    return line 

def defragmenter(line):
    line = list(line.split())
    left = 0
    right = len(line)-1
    while left <= right:

        if line[left] == ".":
            if line[right] != ".":
                line[left], line[right] = line[right], line[left]
                left += 1
                right -= 1
            else:
                right -= 1
        else:
            left += 1
    return " ".join(line)

print(checksum(defragmenter(lineMaker(input_data[0]))))
# 6366665108136