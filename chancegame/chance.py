import time
import random
import os

COIN = 'coin'
DIE = 'die'

dieImageMatrix = []
coinImageMatrix = []

coinsDict = {
    'flipping' : [1,6],
    'heads' : [7,14],
    'tails' : [15,22],
}

dieDict = {
    'rolling' : [1,6],
    'one' : [7,11],
    'two' : [12,16],
    'three' : [17,21],
    'four' : [22,26],
    'five' : [27,31],
    'six' : [32,36],
}

def systemClear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return None

def makeCoins():
    file = open('coins.txt', 'rt')

    for line in file:
        tempList = list(line)
        coinImageMatrix.append(tempList)
    return None

def makeDie():
    file = open('die.txt', 'rt')

    for line in file:
        tempList = list(line)
        dieImageMatrix.append(tempList)
    return None

def decideGame():
    gameInput = (input("Hello! Type 'coin' to flip a coin, type 'die' to roll two die: ")).strip()

    while gameInput != COIN and gameInput != DIE:
        gameInput = (input("That is not 'coin' or 'die', try again: ")).strip()

    return gameInput

def displayStuff(lines, matrix):
    for x in range(lines[0]-1,lines[1]):
        for element in matrix[x]:
            print(element, end='')
    print()
    return None

def coinFlip():
    systemClear()
    displayStuff(coinsDict['flipping'], coinImageMatrix)
    headsOrTails = random.choice(['heads', 'tails'])

    time.sleep(1)
    systemClear()
    displayStuff(coinsDict[headsOrTails], coinImageMatrix)
    print('\n    You flipped', headsOrTails)
    return None

def dieRoll():
    systemClear()
    displayStuff(dieDict['rolling'], dieImageMatrix)
    die1 = random.choice(['one', 'two', 'three', 'four', 'five', 'six'])
    die2 = random.choice(['one', 'two', 'three', 'four', 'five', 'six'])

    time.sleep(1)
    systemClear()
    displayStuff(dieDict[die1], dieImageMatrix)
    displayStuff(dieDict[die2], dieImageMatrix)
    print('You rolled a', die1 ,'and a', die2 )
    return None

def runGame():
    makeCoins()
    makeDie()

    gameType = decideGame()
    gameOn = True

    if gameType == COIN:
        print("Alright, a coin flip it is...")
        time.sleep(1)
        coinFlip()
    elif gameType == DIE:
        print('Alright, a die roll it is...')
        time.sleep(1)
        dieRoll()

    while (gameOn == True):
        counter = 0
        inputGame = 'reset'
        
        while (inputGame != 'c' and inputGame != 'd' and inputGame != 'q'):
            counter += 1
            if counter == 1:
                inputGame = input("\nGo again? Type 'c' to flip a coin, 'd' to roll die, and 'q' to exit: ").strip()
            else:
                inputGame = input("\nThat is not a valid input. Type 'c' to flip a coin, 'd' to roll die, and 'q' to exit: ").strip()

        if inputGame == 'c':
            coinFlip()
        elif inputGame == 'd':
            dieRoll()
        elif inputGame == 'q':
            gameOn = False
    return None

# main
if __name__ == '__main__':
    runGame()
