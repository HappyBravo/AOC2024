# SAUCE : "https://github.com/serpentk/adventofcode2024/blob/master/day3/day3_2.py"
import re
import sys

r = re.compile(r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)")

# memory = ''.join(sys.stdin.readlines())
input_file = "Day03_input.txt"
input_data = []

with open(input_file, "r") as f:
    input_data = f.readlines()

memory = "".join(input_data)
on = True
s = 0
for (enable, disable, x, y) in r.findall(memory):
    print(enable, disable, x, y)
    input()
    if enable:
        on = True
    if disable:
        on = False
    if on and x and y:
        s += int(x) * int(y)
print(s)