input_file = "Day01_input.txt"
input_data = []

left = []
right = []

with open(input_file, "r") as f:
    input_data = f.readlines()
    input_data = [(left.append(int(line.strip().split()[0])), 
                   right.append(int(line.strip().split()[1]))) 
                        for line in input_data]

dictt = {}
for i in right:
    if i in dictt:
        dictt[i] += 1
    else :
        dictt[i] = 1
summ = 0
for i in left:
    if i in dictt:
        summ += i*dictt[i]
    else:
        summ += 0
print(summ) # 20351745