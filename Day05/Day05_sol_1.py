input_file = "Day05_input.txt"
input_data = []

with open(input_file, "r") as f:
    input_data = [_.strip() for _ in f.readlines()]

test =\
"""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
# input_data = [_.strip() for _ in test.splitlines()]

flag = 0
leftOf = {}
rightOf = {}
updates = []

for line in input_data:
    if not line:
        flag = 1
        continue
    if flag:
        updates.append(list(map(int, line.split(","))))
    else:
        [left, right] = list(map(int, line.split('|')))

        if left not in rightOf:
            rightOf[left] = [right]
        else:
            rightOf[left].append(right)

        if right not in leftOf:
            leftOf[right] = [left]
        else:
            leftOf[right].append(left)

summ = 0
for update in updates:
    middlePage = 0
    if all(
            [all([_page in leftOf[page] for _page in update[:idx] if page in leftOf] ) and 
            all([_page in rightOf[page] for _page in update[idx+1:] if page in rightOf] ) 
                                                    for idx, page in enumerate(update)]
        ):
        middlePage = update[len(update)//2]
        summ += middlePage
print(summ)
# 6384
