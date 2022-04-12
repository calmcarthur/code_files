import os
import sys

# unfinished program to compare two files and combine them -- similar to vscodes git extension

def TakeFiles():
    cwd = os.getcwd()

    path1 = cwd + "/" + input("Please enter the path to the master file (not including current working directory): ")
    path2 = cwd + "/" + input("Please enter the path to the comparison file (not including current working directory): ")

    file1 = open("../../Documents/code_repos/7127/DT_Libraries/sensor/o2_sensor/Src/o2_sensor.c", "rt")
    file2 = open("../../7127/DT_Libraries/sensor/o2_sensor/Src/o2_sensor.c", "rt")

    boardMatrix1 = BuildFile(file1)
    boardMatrix2 = BuildFile(file2)

    return boardMatrix1, boardMatrix2


def BuildFile(file):
    boardMatrix = []

    for line in file:
        tempBoardList = list(line)
        boardMatrix.append(tempBoardList)

    return boardMatrix

def DisplayFiles(unofile, duofile):

    masterfile = MakeMasterFile(unofile, duofile)
    sys.stdout = open("Compared_Files.txt", "w")

    for line in masterfile:
        for element in line:
            print(element, end='')
    print()

    return None

def MakeMasterFile(unofile, duofile):

    for line in range(0, len(duofile)):
        for element in range(0, len(duofile[line])):
            unofile[line].append(duofile[line][element])

    return unofile

def FindDifferences(unofile, duofile):
    
    for line in range(0,len(unofile)):
        for i in range(0, len(unofile[line])):
            try:
                test = duofile[line][i]
            except:
                break

            if unofile[line][i] != duofile[line][i]:
                duofile[line][i] = ChangeColour(duofile[line][i])

    return unofile, duofile

def ChangeColour(char):

    # char = "\033[33m" + char + "\033[0m"

    return char

def RunProgram():

    one, two = TakeFiles()

    unofile, duofile = FindDifferences(one, two)

    DisplayFiles(unofile, duofile)

    return None

# main
if __name__ == '__main__':
    RunProgram()

# just combination

"""
import os
import sys

def BuildFile(file):
    boardMatrix = []

    for line in file:
        tempBoardList = list(line)
        boardMatrix.append(tempBoardList)

    return boardMatrix

def GetFiles():
    cwd = os.getcwd()

    path1 = cwd + "/" + input("Please enter the path to the master file (not including current working directory): ")
    path2 = cwd + "/" + input("Please enter the path to the comparison file (not including current working directory): ")

    file1 = open("../../Documents/code_repos/7127/DT_Libraries/sensor/o2_sensor/Src/o2_sensor.c", "rt")
    file2 = open("../../7127/DT_Libraries/sensor/o2_sensor/Src/o2_sensor.c", "rt")

    longestlength = len(max(file1, key=len))

    boardMatrix1 = BuildFile(file1)
    boardMatrix2 = BuildFile(file2)

    return longestlength, boardMatrix1, boardMatrix2

def CombineFiles(longestlength, boardMatrix1, boardMatrix2):
    i = -1
    j = -1
    for lines in boardMatrix1:
        i += 1
        for elements in boardMatrix1[i]:
            j += 1
            currentlinelength = len(boardMatrix1[i])
            howmuchtoadd = longestlength - currentlinelength
            for k in howmuchtoadd:
                boardMatrix1[i] = boardMatrix1[i].append(" ")
            boardMatrix1[i] = boardMatrix1[i].append(boardMatrix2[i][j])
    
    return boardMatrix1

def MakeMasterFile(boardMatrix1):
    sys.stdout = open("Compared_Files.txt", "w")
    for line in boardMatrix1:
        for element in line:
            print(element, end='')
    print()

    return None

def RunProgram():
    longestlength, boardMatrix1, boardMatrix2 = GetFiles()
    boardMatrix = CombineFiles(longestlength, boardMatrix1, boardMatrix2)
    MakeMasterFile(boardMatrix)

if __name__ == "__main__":
    RunProgram()
"""