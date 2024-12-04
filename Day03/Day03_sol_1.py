input_file = "Day03_input.txt"
input_data = []

with open(input_file, "r") as f:
    input_data = f.readlines()

summ = 0
for line in input_data:
    splitted = [splitt.split(')') for splitt in line.strip().split('mul(')]

    for splitt in splitted:
        nums = [0, 0]
        nums = splitt[0].split(",")
        try :
            num1 = int(nums[0])
            num2 = int(nums[1])
            summ += num1*num2

        except Exception as e:
            print(f"Exception {e}")
print(summ) # 182619815