input_file = "Day01_input.txt"
input_data = []

left = []
right = []

with open(input_file, "r") as f:
    input_data = f.readlines()
    input_data = [(left.append(int(line.split()[0])), 
                   right.append(int(line.split()[1]))) 
                        for line in input_data]

left.sort()
right.sort()

assert(len(left) == len(right))

summ = 0
for l, r in zip(left, right):
    summ += abs(l-r)
print(summ) # 1579939
