import os
import sys
import time

def Count1File(fullpath, countCommand=False):
    # How many line of code is in the file
    count = 0
    text = open(fullpath, 'r').read()
    line = text.count('\n') + 1
    text = text.split('\n')
    for x in range(line):
        text[x] = text[x].strip()
    #
    if fullpath.endswith(".py") or fullpath.endswith(".pyw") or fullpath.endswith(".py3") or fullpath.endswith(".py2"):
        beginCommand = "#"
    elif fullpath.endswith(".cpp") or fullpath.endswith(".json"):
        beginCommand = "/"
    
    for x in range(line):
        if not (text[x].startswith(beginCommand) or countCommand):
            count += 1
    return count


def run(filepath, search=("py")):
    if os.path.isfile(filepath):
        raise ValueError("Must be a file Folder")
        
    line = 0
    AllFiles = os.listdir(filepath)
    print(AllFiles)
    for file in AllFiles:
        if file == ".git":
            continue
            
        fullpath = os.path.join(filepath, file)
        print(f"file: {file}, fullpath: {fullpath}")
        if os.path.isfile(file) and file.endswith(search):
            line += Count1File(file)
        elif not os.path.isfile(fullpath):
            line += run(fullpath, search=search)

    return line

if __name__ == '__main__':
    x=run("C:\\Users\\Admin\\Desktop\\HTML\\CountLineOfCode")
    print(x)
