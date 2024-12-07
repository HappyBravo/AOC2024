input_file = "Day07_input.txt"
input_data = []

with open(input_file, "r") as f:
    input_data = [_.strip() for _ in f.readlines()]

test = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
# input_data = [_.strip() for _ in test.splitlines()]

def doOperation(operands, operations, curr_expression = "", i = 0, expressions = []):
    if i >= len(operands)-1:
        expressions.append(f"{curr_expression}")
        return
    for operation in operations:
        doOperation(operands, operations, 
                    curr_expression = f"({curr_expression}{operation}{operands[i+1]})",
                    i = i+1, expressions=expressions)

operations = ['+', '*']
def findOperation(operands, result, operations = operations):
    expressions = []
    doOperation(operands=operands, operations=operations,  
                curr_expression=f"{operands[0]}",
                i=0, expressions=expressions)
    
    results = []
    for expression in expressions:
        _result = eval(expression)
        if _result == result:
            # print(f"{result} : {expression}")
            results.append((_result, expression))  
    return len(results) 


countt, summ = 0, 0
for line in input_data:
    print(line)
    result, operands = line.split(":")
    result = int(result)
    operands = list(map(int, operands.strip().split()))

    if(findOperation(operands=operands, result=result)):
        countt+=1
        summ += result
print(countt, summ)
# 356 5837374519342
