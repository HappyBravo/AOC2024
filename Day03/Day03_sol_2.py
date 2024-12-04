input_file = "Day03_input.txt"
input_data = []

with open(input_file, "r") as f:
    input_data = f.readlines()

def mul(line=""): # TAKEN FROM DAY3, SOL1
    summ = 0
    if "mul(" in line: 
        splitted = [splitt.split(')') for splitt in line.strip().split('mul(')]

        for splitt in splitted:
            nums = [0, 0]
            nums = splitt[0].split(",")
            try :
                num1 = int(nums[0])
                num2 = int(nums[1])
                summ += num1*num2
                # print(f"{num1} x {num2} = {num1*num2}")

            except Exception as e:
                # print(f"Exception {e}")
                pass
    return summ

flag = 1 # UNCOMMENT THIS LINE TO GET WRONG 2 AND THE CORRECT 
summ = 0
test = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

input_data = ["".join(input_data)]  # UNCOMMENT THIS LINE TO GET THE CORRECT, 
                                    # WE NEED TO MAKE THE WHOLE INPUT DATA TO ONE LINE 
                                    # I WASTED WHOLE 5 HRS TRYING TO FIND WHY MY CODE WAS NOT WORKING 😑
for line in input_data :
# for line in test :
    lines = []
    # print(line)
    # flag = 1 # UNCOMMENT THIS LINE TO GET WRONG 1
    todos = []
    lines += line.split("don't()")
    for _line in lines:
        # print(">>>", _line)
        todo = []
        if flag :
            summ += mul(_line)
            flag = 0
            continue
        todos = _line.split("do()")[1:]
        for todo in todos:
            # print("todo---",doto)
            # input()
            summ += mul(todo)
        flag = 0
    #     print()
    # print()
    # input()
print(summ)

# 85770822 < WRONG 1
# 74181237 < WRONG 2
# 80747545 < RIGHT ONE, FINALLY
