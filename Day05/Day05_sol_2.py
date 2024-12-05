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

def isCorrect(update): # TAKEN FROM PART 1
    global wrongFlag
    if all(
            [all([_page in leftOf[page] for _page in update[:idx] if page in leftOf] ) and 
            all([_page in rightOf[page] for _page in update[idx+1:] if page in rightOf] ) 
                                                    for idx, page in enumerate(update)]
        ):
        return True
    wrongFlag = True
    return False

def swap(pages, indx1, indx2):
    pages[indx1], pages[indx2] = pages[indx2], pages[indx1]
    return pages

summ = 0
for update in updates:
    wrongFlag = False
    middlePage = 0
    while not isCorrect(update):
        flag = 0
        for idx, page in enumerate(update):
            leftSide = update[:idx]
            rightSide = update[idx+1:]

            for _page in leftSide:
                if _page in leftOf and page in leftOf[_page]: # CHECK WRONG ORDERING
                    print(f"Error in {update} - in {_page} and {page}")
                    errPage_indx = update.index(page)
                    err_Page_indx = update.index(_page)
                    update = swap(update, errPage_indx, err_Page_indx)
                    flag = 1
                    break
            if flag:
                break # RE-CHECK THE CORRECTNESS
            for _page in rightSide:
                if _page in rightOf and page in rightOf[_page]: # CHECK WRONG ORDERING
                    print(f"Error in {update} - in {page} and {_page}")
                    errPage_indx = update.index(page)
                    err_Page_indx = update.index(_page)
                    update = swap(update, errPage_indx, err_Page_indx)
                    break
    if wrongFlag:
        middlePage = update[len(update)//2]
        summ += middlePage

print(summ)
# 5353
