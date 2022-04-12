import string
import time
import random
import os
import curses


# set operating system for program
windowsOrLinux = ''
if os.name == 'nt':
    import msvcrt
    windowsOrLinux = 'win'
else:
    from getch import getch
    windowsOrLinux = 'lin'

# global variables
boardMatrix = []
genNum = []
currentNum = []
prevNums = []
acceptedInputs = ['0','1','2','3','4','5','6','7','8','9','\r','\x08','\x7f']
colCounter = 1
rowCounter = 1
stringGenNum = ''
gameOn = True
tileChanges = []

# generate random number
def ChooseNum():
    global stringGenNum

    for i in range(0,5):
        number = str(random.randint(0,9))
        tempInt = [i+1, number]
        stringGenNum += number
        genNum.append(tempInt)

    return None

# build board matrix
def BuildBoard():
    global boardMatrix

    file = open("numero_board.txt", "rt")
    for line in file:
        tempBoardList = list(line)
        boardMatrix.append(tempBoardList)

    return None

# display the board on screen
def DisplayBoard():
    global boardMatrix

    for line in boardMatrix:
        for element in line:
            print(element, end='')
    print()

    return None

# modify game / board when enter specifically is pressed
def onEnter():
    global gameOn
    global currentNum
    global prevNums
    global genNum
    global rowCounter
    global colCounter
    global stringGenNum

    if currentNum == genNum:
        gameOn = False
        print("Congratulations, you guessed the number " + stringGenNum + "correctly. Thanks for playing.")
        input("Press 'enter' to exit: ")

    elif rowCounter == 5:
        gameOn = False
        print("Sorry, you did not guess the number in time. The number was: " + stringGenNum + ". Thanks for playing.")
        input("Press 'enter' to exit: ")

    else:
        
        EnterColourChange()

        prevNums.append(currentNum)
        currentNum = []

        rowCounter = rowCounter + 1
        colCounter = 1

        SystemClear()

    return None

# changes the colour of the box around the number
def ChangeBoxColour(colour, col):
    global boardMatrix
    global rowCounter
    global colCounter

    boardMatrix[(rowCounter*5) + 3][(col*8) - 5] = "\033[" + colour + "m|\033[0m"
    boardMatrix[(rowCounter*5) + 3][(col*8) + 1] = "\033[" + colour + "m|\033[0m"
    boardMatrix[(rowCounter*5) + 2][(col*8) + 1] = "\033[" + colour + "m|\033[0m"
    boardMatrix[(rowCounter*5) + 2][(col*8) - 5] = "\033[" + colour + "m|\033[0m"
    boardMatrix[(rowCounter*5) + 4][(col*8) + 1] = "\033[" + colour + "m|\033[0m"
    boardMatrix[(rowCounter*5) + 4][(col*8) - 5] = "\033[" + colour + "m|\033[0m"
    
    boardMatrix[(rowCounter*5) + 1][(col*8) - 3] = "\033[" + colour + "m_\033[0m"
    boardMatrix[(rowCounter*5) + 1][(col*8) - 4] = "\033[" + colour + "m_\033[0m"
    boardMatrix[(rowCounter*5) + 1][(col*8) - 2] = "\033[" + colour + "m_\033[0m"
    boardMatrix[(rowCounter*5) + 1][(col*8) - 1] = "\033[" + colour + "m_\033[0m"
    boardMatrix[(rowCounter*5) + 1][(col*8) - 0] = "\033[" + colour + "m_\033[0m"

    boardMatrix[(rowCounter*5) + 5][(col*8) - 3] = "\033[" + colour + 'm"\033[0m'
    boardMatrix[(rowCounter*5) + 5][(col*8) - 0] = "\033[" + colour + 'm"\033[0m'
    boardMatrix[(rowCounter*5) + 5][(col*8) - 4] = "\033[" + colour + 'm"\033[0m'
    boardMatrix[(rowCounter*5) + 5][(col*8) - 2] = "\033[" + colour + 'm"\033[0m'
    boardMatrix[(rowCounter*5) + 5][(col*8) - 1] = "\033[" + colour + 'm"\033[0m'

    return None

# clear the screen
def SystemClear():
    os.system('cls' if os.name == 'nt' else 'clear')
    DisplayBoard()

    return None

# colour logic for tiles and colours
def EnterColourChange():
    global boardMatrix
    global currentNum
    global genNum
    global rowCounter
    global colCounter
    global stringGenNum
    # check if there are correct nums, and correct nums + spots. Change colours, tiles. Tiles are the indication for OnTheGo.
    
    for i in range(0,5):

        if currentNum[i][1] in stringGenNum:
            colour = '33'
            col = currentNum[i][0]
            boardMatrix[(rowCounter*5) + 3][(col*8) -2] = "\033[" + colour + "m" + currentNum[i][1] + "\033[0m"
            ChangeBoxColour(colour, col)
            ChangeTile(colour, currentNum[i][1])

        if currentNum[i] in genNum[i]:
            colour = '32'
            col = currentNum[i][0]
            boardMatrix[(rowCounter*5) + 3][(col*8) -2] = "\033[" + colour + "m" + currentNum[i][1] + "\033[0m"
            ChangeBoxColour(colour, col)
            ChangeTile(colour, currentNum[i][1])

    SystemClear()

    return None

def ChangeTile(colour, num):
    global tileChanges

    tileChanges.append([num, colour])
    boardMatrix[32][(int(num)*4)+4] = "\033[" + colour + "m" + num + "\033[0m"

    return None

# colour change and number change as typed
def OnGoChange(stringInput):
    global boardMatrix
    global currentNum
    global genNum
    global rowCounter
    global colCounter
    global tileChanges

    if len(tileChanges) > 0:
        for i in range(0,len(tileChanges)):
            if stringInput in tileChanges[i]:
                colour = tileChanges[i][1]
            
            else:
                colour = "0"
    
    else:
        colour = "0"

    boardMatrix[(rowCounter*5) + 3][(colCounter*8) - 2] = "\033[" + colour + "m" + stringInput + "\033[0m"
    ChangeBoxColour(colour, colCounter)

    return None

# input driver and verification
def TakeInput():
    global colCounter
    global rowCounter
    global currentNum
    global prevNums
    global gameOn

    stringInput = ""

    print("Welcome to Numero. The game is the exact same as WORDLE, just with 5 digit numbers. Enjoy!")
    time.sleep(3)

    while gameOn == True:
    
        # check system
        if windowsOrLinux == 'win':
            colourpress = msvcrt.getch()
            stringInput = colourpress.decode()
        else:
            stringInput = getch()

        # quit command
        if stringInput == 'q':
            gameOn = False
            continue

        # input switches and board mods
        if stringInput in acceptedInputs:
            if stringInput == '\r':
                if colCounter == 6:
                    if currentNum not in prevNums:
                        onEnter()

            elif stringInput == '\x08' or stringInput == '\x7f':
                if colCounter != 1:
                    ChangeBoard(stringInput)

            else:
                if colCounter == 6:
                    continue

                currentNum.append([colCounter, stringInput])
                ChangeBoard(stringInput)

    return None

# modify the board for non-enter presses
def ChangeBoard(stringInput):
    global rowCounter
    global colCounter
    global boardMatrix
    global currentNum

    # backspace
    if stringInput == '\x08' or stringInput == '\x7f':
        colCounter = colCounter - 1
        del currentNum[colCounter-1]
        stringInput = " "
        OnGoChange(stringInput)
    
    # number
    else:    
        OnGoChange(stringInput)
        colCounter += 1
    
    SystemClear()

    return None

# run the game
def RunGame():
    BuildBoard()
    ChooseNum()

    SystemClear()
    TakeInput()

    return None

# main
if __name__ == '__main__':
    RunGame()