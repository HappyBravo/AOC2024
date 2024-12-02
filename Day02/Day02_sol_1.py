input_file = "Day02_input.txt"
input_data = []

with open(input_file, "r") as f:
    input_data = f.readlines()

def check(levels):
    prev_diff = 0
    print()
    for i, level in enumerate(levels[1:], start=1):
        diff = level - levels[i-1]
        if not diff:
            print(f"diff is 0, {levels[i-1]}, {level}")
            return False
        if abs(diff) > 3:
            print(f"diff is >3, {levels[i-1]}, {level}")
            return False
    
        if prev_diff:
            if (diff/abs(diff) != prev_diff/abs(prev_diff)):
                print(f"sign is changing {levels[i-1]}, {level}")
                return False
        prev_diff = diff
    return True

# print(input_data)
checks = []
for line in input_data:
    line = line.strip()
    levels = list(map(int, line.split()))
    checked = check(levels)
    print(f"{levels} : {checked}")
    checks.append(checked)
print(len([i for i in checks if i])) # 472

