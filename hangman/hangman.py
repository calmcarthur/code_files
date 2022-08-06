import random
import time
import linecache
import os
from typing import List

boardMatrix = []
chosenLetters = []
rightLetters = []
wrongLetters = []
firstGuessCounter = 0

letterLocations = {
    'a' : [15, 33],
    'b' : [15, 36],
    'c' : [15, 39],
    'd' : [15, 42],
    'e' : [15, 45],
    'f' : [16, 33],
    'g' : [16, 36],
    'h' : [16, 39],
    'i' : [16, 42],
    'j' : [16, 45],
    'k' : [17, 33],
    'l' : [17, 36],
    'm' : [17, 39],
    'n' : [17, 42],
    'o' : [17, 45],
    'p' : [18, 33],
    'q' : [18, 36],
    'r' : [18, 39],
    's' : [18, 42],
    't' : [18, 45],
    'u' : [19, 33],
    'v' : [19, 36],
    'w' : [19, 39],
    'x' : [19, 42],
    'y' : [19, 45],
    'z' : [20, 33],
}

def SystemClear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return None

def BuildBoard():
    file = open('hangmanempty.txt', 'rt')
    for line in file:
        tempBoardList = list(line)
        tempBoardList.remove('\n')
        boardMatrix.append(tempBoardList)
    return None

def DisplayBoard():
    for line in boardMatrix:
        for element in line:
            print(element, end='')
        print()
    return None

def GenerateWord():
    file = open('words.txt', 'rt')
    randomLine = random.randrange(1, 850, 1)
    randomWord = linecache.getline('words.txt', randomLine)
    randomWord = randomWord.strip()
    file.close()
    randomWordLength = len(randomWord.strip())
    return randomWord, randomWordLength

def GetLetter():
    chosenLetter = str()
    acceptedInputs = {'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z'}
    newGuessCounter = 0
    global firstGuessCounter

    while chosenLetter not in acceptedInputs:
        SystemClear()
        DisplayBoard()        
        newGuessCounter += 1

        if firstGuessCounter == 0: 
            chosenLetter = input("Ready to go? First, choose a letter: ")
            chosenLetter.strip()
            if chosenLetter.isupper() == True:
                chosenLetter = chosenLetter.swapcase()
            firstGuessCounter += 1
            time.sleep(0.5)
            continue

        if newGuessCounter == 1:
            chosenLetter = input('Choose a letter: ')
            chosenLetter.strip()
            if chosenLetter.isupper() == True:
                chosenLetter = chosenLetter.swapcase()
            time.sleep(0.5)
        else: 
            chosenLetter = input("Sorry, that is not a valid letter. Try again: ")
            chosenLetter.strip()
            if chosenLetter.isupper() == True:
                chosenLetter = chosenLetter.swapcase()
            time.sleep(0.5)

        repeatBool = CheckRepeat(chosenLetter)
        if repeatBool == True:
            SystemClear()
            DisplayBoard()
            chosenLetter = input("That letter has already been chosen. Try again: ")
            chosenLetter.strip()
            if chosenLetter.isupper() == True:
                chosenLetter = chosenLetter.swapcase()
            time.sleep(0.5)
        
    return chosenLetter

def AddLimb(numberWrong):
    global boardMatrix
    if numberWrong == 1:
        # head
        boardMatrix[4][16] = '_'
        boardMatrix[4][18] = '_'
        boardMatrix[5][19] = '\\'
        boardMatrix[6][20] = '\\'
        boardMatrix[7][20] = '/'
        boardMatrix[8][19] = '/'
        boardMatrix[8][18] = '_'
        boardMatrix[8][17] = '_'
        boardMatrix[8][16] = '_'
        boardMatrix[8][15] = '\\'
        boardMatrix[7][14] = '\\'
        boardMatrix[6][14] = '/'
        boardMatrix[5][15] = '/'
    if numberWrong == 2:
        # body
        boardMatrix[9][17] = '|'
        boardMatrix[10][17] = '|'
        boardMatrix[11][17] = '|'
        boardMatrix[12][17] = '|'
        boardMatrix[13][17] = '|'
        boardMatrix[14][17] = '|'
        boardMatrix[15][17] = '|'
    if numberWrong == 3:
        # right leg
        boardMatrix[16][18] = '\\'
        boardMatrix[17][19] = '\\'
        boardMatrix[18][20] = '\\'
        boardMatrix[19][21] = '\\'
    if numberWrong == 4:
        # left arm
        boardMatrix[11][16] = '_'
        boardMatrix[11][15] = '_'
        boardMatrix[11][14] = '_'
        boardMatrix[12][13] = '/'
        boardMatrix[13][12] = '/'
        boardMatrix[14][11] = '/'
    if numberWrong == 5:
        # right shoe
        boardMatrix[20][21] = '|'
        boardMatrix[20][24] = '|'
        boardMatrix[20][23] = '_'
        boardMatrix[20][22] = '_'
        boardMatrix[19][23] = '_'
        boardMatrix[19][22] = '_'
    if numberWrong == 6:
        # left leg
        boardMatrix[16][16] = '/'
        boardMatrix[17][15] = '/'
        boardMatrix[18][14] = '/'
        boardMatrix[19][13] = '/'
    if numberWrong == 7:
        # left shoe
        boardMatrix[19][12] = '_'
        boardMatrix[19][11] = '_'
        boardMatrix[20][10] = '|'
        boardMatrix[20][11] = '_'
        boardMatrix[20][12] = '_'
        boardMatrix[20][13] = '|'
    if numberWrong == 8:
        # right arm
        boardMatrix[9][23] = '/'
        boardMatrix[10][22] = '/'
        boardMatrix[11][21] = '/'
        boardMatrix[11][20] = '_'
        boardMatrix[11][19] = '_'
        boardMatrix[11][18] = '_'
    return None

def UpdateLetters(chosenLetter):
    global boardMatrix
    for key in letterLocations:
        if key == chosenLetter:
            boardMatrix[letterLocations[key][0]][letterLocations[key][1]] = ' '
    return None

def WordLengthSet(wordLength):
    global boardMatrix
    for i in range(0, wordLength-1):
        boardMatrix[15][59 + 2*(i)] = '_'
    return None

def CheckRepeat(chosenLetter):
    global chosenLetters
    if chosenLetter in chosenLetters:
        repeatBool = True
    else:
        repeatBool = False
    return repeatBool

def AddLetter(gameWord, currentLetter):
    global boardMatrix
    letterCounter = -1
    spacesToChange = []
    gameWordList = list(gameWord)
    for element in gameWordList:
        letterCounter += 1
        if currentLetter == element:
            spacesToChange.append(letterCounter)
    for i in spacesToChange:
        boardMatrix[15][57 + 2*(i)] = currentLetter
    return None

def GameRunning():
    BuildBoard()
    gameWord, gameWordLength = GenerateWord()[0:2]
    WordLengthSet(gameWordLength)

    global chosenLetters
    global rightLetters
    global wrongLetters
    endGame = False

    wrongCounter = 0

    while endGame == False:
        currentChosenLetter = GetLetter()
        UpdateLetters(currentChosenLetter)
        chosenLetters.append(currentChosenLetter)

        if currentChosenLetter in gameWord:
            rightLetters.append(currentChosenLetter)
            if set(rightLetters) == set(gameWord):
                AddLetter(gameWord, currentChosenLetter)
                SystemClear()
                DisplayBoard()
                print("YOU WON. Congratulations! You got the word", gameWord, "in", len(chosenLetters), "tries!")
                time.sleep(3)
                input("Press enter to exit. Thanks for playing!")
                endGame = True
                continue
            AddLetter(gameWord, currentChosenLetter)
            print(currentChosenLetter, "is in the word. Good job, keep going!")
            time.sleep(2)
        else:
            wrongLetters.append(currentChosenLetter)
            wrongCounter += 1
            if wrongCounter == 8:
                AddLimb(wrongCounter)
                SystemClear()
                DisplayBoard()
                print("Oh no... you hanged the hangman. The word was:", gameWord, "\nPlay again soon!")
                time.sleep(3)
                input("Press enter to exit. Thanks for playing!")
                endGame = True
                continue
            AddLimb(wrongCounter)
            print(currentChosenLetter, "is not in the word. New limb added.")
            time.sleep(2)
    
    return None

# main
GameRunning()

# bugs : win sequence -- convert to set, repeated letter after a repeated letter 