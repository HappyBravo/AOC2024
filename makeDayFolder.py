import os 
import pathlib

cwd = pathlib.Path().resolve()
print(cwd)

days = [f for f in os.listdir(cwd) if f.lower().startswith("day") and
                                                os.path.isdir(os.path.join(cwd, f))]
# print(days)

# files to create
files = {
            "input" : "input", 
            "ques" : "ques", 
            "sol" : "sol" 
        }

def checkDay(dayFolderPath, day):
    print(dayFolderPath)
    dayFolder = os.path.basename(dayFolderPath)
    print(dayFolder)
    
    assert dayFolder.lower().startswith("day") and os.path.isdir(dayFolderPath)

    _day = int(dayFolder[3:])
    print(_day)

    if day == _day:
        print(f"Day {day} folder already present !!!")
        return False
    return True

day = int(input("Which day ? : "))

flag = True
for _day in days:
    if str(day) in _day:
        _ = os.path.join(cwd, _day)
        flag = checkDay(_, day)

if flag :
    daySuffix = f"{'0'+str(day) if day<10 else day}"
    folderName = f"Day{daySuffix}"
    newFolderPath = os.path.join(cwd, folderName)
    pyFiles = [os.path.join(newFolderPath, f"{folderName}_{files['sol']}_{num}.py") 
                                                                    for num in range(1,3)]
    quesFiles = [os.path.join(newFolderPath, f"{folderName}_{files['ques']}_{num}.txt") 
                                                                    for num in range(1,3)]
    inputFiles = [os.path.join(newFolderPath, f"{folderName}_{files['input']}.txt")]
    
    print(folderName)

    os.makedirs(os.path.join(cwd, folderName))
    filesToMake = pyFiles+quesFiles+inputFiles

    for filee in filesToMake:
        buff = ""
        if filee.endswith(".py"):
            buff = \
f"""input_file = "{os.path.basename(inputFiles[0])}"
input_data = []

with open(input_file, "r") as f:
    input_data = [_.strip() for _ in f.readlines()]
"""
        with open(filee, "w", encoding="utf-8") as _f:
            _f.write(buff)
        print(f"'{filee}' - made")